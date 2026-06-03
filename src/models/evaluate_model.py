"""Held-out model evaluation utilities."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_recall_curve,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.pipeline import Pipeline


def evaluate_classifier(
    pipeline: Pipeline,
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> dict[str, object]:
    """Evaluate a fitted classifier pipeline on the held-out test set."""
    y_pred = pipeline.predict(X_test)
    y_score = pipeline.predict_proba(X_test)[:, 1]
    matrix = confusion_matrix(y_test, y_pred)

    return {
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "precision": float(precision_score(y_test, y_pred, zero_division=0)),
        "recall": float(recall_score(y_test, y_pred, zero_division=0)),
        "f1": float(f1_score(y_test, y_pred, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_test, y_score)),
        "confusion_matrix": matrix,
        "classification_report": classification_report(
            y_test,
            y_pred,
            target_names=["No churn", "Churn"],
            zero_division=0,
        ),
        "y_pred": y_pred,
        "y_score": y_score,
    }


def save_confusion_matrix_figure(
    matrix,
    output_path: str | Path,
) -> None:
    """Save the confusion matrix figure."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(6, 5))
    display = ConfusionMatrixDisplay(
        confusion_matrix=matrix,
        display_labels=["No churn", "Churn"],
    )
    display.plot(ax=ax, cmap="Blues", colorbar=False, values_format="d")
    ax.set_title("Held-out Confusion Matrix")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def save_roc_curve_figure(
    pipeline: Pipeline,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    output_path: str | Path,
) -> None:
    """Save the ROC curve figure."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(6, 5))
    RocCurveDisplay.from_estimator(pipeline, X_test, y_test, ax=ax)
    ax.set_title("Held-out ROC Curve")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def save_precision_recall_curve_figure(
    y_test: pd.Series,
    y_score,
    output_path: str | Path,
) -> None:
    """Save the precision-recall curve figure."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    precision, recall, _ = precision_recall_curve(y_test, y_score)
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(recall, precision)
    ax.set_title("Held-out Precision-Recall Curve")
    ax.set_xlabel("Recall")
    ax.set_ylabel("Precision")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def write_evaluation_report(
    metrics: dict[str, object],
    output_path: str | Path,
    model_name: str,
) -> None:
    """Write the held-out evaluation summary."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    tn, fp, fn, tp = metrics["confusion_matrix"].ravel()
    markdown = [
        "# Held-out Model Evaluation Summary",
        "",
        "## Scope",
        "",
        "This report documents Phase 07 held-out test evaluation. The selected baseline model is fit on the training split only and evaluated once on the held-out test set.",
        "",
        "No hyperparameters or thresholds are tuned on the held-out test set.",
        "",
        "## Selected Model",
        "",
        f"- `{model_name}`",
        "- Full pipeline: preprocessing + classifier",
        "- Classification threshold: default `0.5`",
        "",
        "## Held-out Test Metrics",
        "",
        f"- Accuracy: `{metrics['accuracy']:.4f}`",
        f"- Precision: `{metrics['precision']:.4f}`",
        f"- Recall: `{metrics['recall']:.4f}`",
        f"- F1 score: `{metrics['f1']:.4f}`",
        f"- ROC-AUC: `{metrics['roc_auc']:.4f}`",
        "",
        "## Confusion Matrix",
        "",
        "| Actual / Predicted | No churn | Churn |",
        "| --- | ---: | ---: |",
        f"| No churn | {tn} | {fp} |",
        f"| Churn | {fn} | {tp} |",
        "",
        "For churn detection, false negatives are customers who churned but were predicted as no churn. These are especially costly because the business may miss the opportunity to intervene.",
        "",
        f"- False negatives: `{fn}`",
        f"- True positives: `{tp}`",
        "",
        "Recall measures how many actual churn customers the model caught. ROC-AUC measures how well the model ranks churn risk across thresholds, without choosing a custom threshold on the test set.",
        "",
        "## Classification Report",
        "",
        "```text",
        str(metrics["classification_report"]).strip(),
        "```",
        "",
        "## Generated Figures",
        "",
        "- `reports/figures/confusion_matrix.png`",
        "- `reports/figures/roc_curve.png`",
        "- `reports/figures/precision_recall_curve.png`",
        "",
        "## Status Note",
        "",
        "Phase 08 added model interpretation, limitations, and business recommendations without retuning on the held-out test set.",
        "",
    ]
    path.write_text("\n".join(markdown), encoding="utf-8")
