"""Evaluate the selected baseline model on the held-out test set."""

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd

from src.features.build_features import ID_COLUMN, TARGET_COLUMN, create_train_test_split
from src.models.evaluate_model import (
    evaluate_classifier,
    save_confusion_matrix_figure,
    save_precision_recall_curve_figure,
    save_roc_curve_figure,
    write_evaluation_report,
)
from src.models.train_model import build_training_pipeline, get_baseline_models


CLEANED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "telco_customer_churn_cleaned.csv"
REPORT_PATH = PROJECT_ROOT / "reports" / "model_evaluation_summary.md"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"
SELECTED_MODEL_NAME = "logistic_regression"


def main() -> None:
    """Run Phase 07 held-out evaluation."""
    data = pd.read_csv(CLEANED_DATA_PATH)
    split = create_train_test_split(data)

    estimator = get_baseline_models()[SELECTED_MODEL_NAME]
    pipeline = build_training_pipeline(estimator, split.X_train)

    # Fit only on train; the held-out test set is used below only once.
    pipeline.fit(split.X_train, split.y_train)
    metrics = evaluate_classifier(pipeline, split.X_test, split.y_test)

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    save_confusion_matrix_figure(
        metrics["confusion_matrix"],
        FIGURES_DIR / "confusion_matrix.png",
    )
    save_roc_curve_figure(
        pipeline,
        split.X_test,
        split.y_test,
        FIGURES_DIR / "roc_curve.png",
    )
    save_precision_recall_curve_figure(
        split.y_test,
        metrics["y_score"],
        FIGURES_DIR / "precision_recall_curve.png",
    )
    write_evaluation_report(metrics, REPORT_PATH, SELECTED_MODEL_NAME)

    tn, fp, fn, tp = metrics["confusion_matrix"].ravel()
    print(f"Cleaned dataset: {CLEANED_DATA_PATH}")
    print(f"Selected model: {SELECTED_MODEL_NAME}")
    print(f"Target column: {TARGET_COLUMN}")
    print(f"Excluded ID column: {ID_COLUMN}")
    print(f"Train shape: {split.X_train.shape}")
    print(f"Test shape: {split.X_test.shape}")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(f"Precision: {metrics['precision']:.4f}")
    print(f"Recall: {metrics['recall']:.4f}")
    print(f"F1 score: {metrics['f1']:.4f}")
    print(f"ROC-AUC: {metrics['roc_auc']:.4f}")
    print(f"Confusion matrix: TN={tn}, FP={fp}, FN={fn}, TP={tp}")
    print(f"Evaluation summary: {REPORT_PATH}")
    print(f"Figures directory: {FIGURES_DIR}")


if __name__ == "__main__":
    main()
