"""Baseline model training and comparison utilities."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, make_scorer, precision_score, recall_score
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline

from src.features.build_features import RANDOM_SEED, build_preprocessing_pipeline


BASELINE_SCORING = {
    "roc_auc": "roc_auc",
    "accuracy": "accuracy",
    "precision": make_scorer(precision_score, zero_division=0),
    "recall": make_scorer(recall_score, zero_division=0),
    "f1": make_scorer(f1_score, zero_division=0),
}


def get_baseline_models(random_state: int = RANDOM_SEED) -> dict[str, object]:
    """Return a small set of baseline classifiers."""
    return {
        "dummy_most_frequent": DummyClassifier(strategy="most_frequent"),
        "logistic_regression": LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=random_state,
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=100,
            class_weight="balanced",
            random_state=random_state,
            n_jobs=-1,
        ),
    }


def build_training_pipeline(estimator: object, X_train: pd.DataFrame) -> Pipeline:
    """Build a full training pipeline with preprocessing and estimator."""
    return Pipeline(
        steps=[
            ("preprocessor", build_preprocessing_pipeline(X_train)),
            ("model", estimator),
        ]
    )


def compare_baseline_models(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    models: dict[str, object] | None = None,
    cv_splits: int = 5,
    random_state: int = RANDOM_SEED,
) -> pd.DataFrame:
    """Compare baseline models with stratified cross-validation on train data."""
    if models is None:
        models = get_baseline_models(random_state=random_state)

    cv = StratifiedKFold(
        n_splits=cv_splits,
        shuffle=True,
        random_state=random_state,
    )

    rows: list[dict[str, float | str]] = []
    for model_name, estimator in models.items():
        pipeline = build_training_pipeline(estimator, X_train)
        scores = cross_validate(
            pipeline,
            X_train,
            y_train,
            cv=cv,
            scoring=BASELINE_SCORING,
            n_jobs=1,
            error_score="raise",
        )

        row: dict[str, float | str] = {"model": model_name}
        for metric_name in BASELINE_SCORING:
            metric_scores = scores[f"test_{metric_name}"]
            row[f"{metric_name}_mean"] = float(metric_scores.mean())
            row[f"{metric_name}_std"] = float(metric_scores.std())
        rows.append(row)

    results = pd.DataFrame(rows)
    return results.sort_values(
        by=["roc_auc_mean", "recall_mean", "f1_mean"],
        ascending=False,
    ).reset_index(drop=True)


def fit_baseline_pipelines(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    models: dict[str, object] | None = None,
    random_state: int = RANDOM_SEED,
) -> dict[str, Pipeline]:
    """Fit baseline pipelines on train data after comparison."""
    if models is None:
        models = get_baseline_models(random_state=random_state)

    fitted_pipelines: dict[str, Pipeline] = {}
    for model_name, estimator in models.items():
        pipeline = build_training_pipeline(estimator, X_train)
        fitted_pipelines[model_name] = pipeline.fit(X_train, y_train)
    return fitted_pipelines


def write_model_comparison_report(
    results: pd.DataFrame,
    output_path: str | Path,
) -> None:
    """Write a concise markdown report for baseline model comparison."""
    report_path = Path(output_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    best_model = results.iloc[0]
    markdown_table = _dataframe_to_markdown_table(results.round(4))
    markdown = [
        "# Baseline Model Training Summary",
        "",
        "## Scope",
        "",
        "This report documents Phase 06 baseline model training. It compares a small set of scikit-learn classifiers using stratified cross-validation on the training split only.",
        "",
        "The held-out test set is not used for model selection in this phase. Final evaluation belongs to Phase 07.",
        "",
        "## Models Compared",
        "",
        "- `DummyClassifier(strategy=\"most_frequent\")`",
        "- `LogisticRegression(class_weight=\"balanced\")`",
        "- `RandomForestClassifier(class_weight=\"balanced\")`",
        "",
        "## Cross-Validation Results",
        "",
        markdown_table,
        "",
        "## Current Best Baseline",
        "",
        f"- Best ROC-AUC: `{best_model['model']}` with ROC-AUC `{best_model['roc_auc_mean']:.4f}`.",
        f"- Recall for that model: `{best_model['recall_mean']:.4f}`.",
        "",
        "Because churn detection cares about identifying at-risk customers, recall and ROC-AUC should remain important during Phase 07 evaluation.",
        "",
        "## Status Note",
        "",
        "The selected logistic regression baseline was later evaluated once on the held-out test set in Phase 07.",
        "",
    ]

    report_path.write_text("\n".join(markdown), encoding="utf-8")


def _dataframe_to_markdown_table(data: pd.DataFrame) -> str:
    """Render a small DataFrame as a markdown table without extra packages."""
    columns = list(data.columns)
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for _, row in data.iterrows():
        values = [str(row[column]) for column in columns]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)
