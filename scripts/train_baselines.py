"""Train and compare baseline churn classifiers."""

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd

from src.features.build_features import (
    ID_COLUMN,
    TARGET_COLUMN,
    create_train_test_split,
)
from src.models.train_model import (
    compare_baseline_models,
    fit_baseline_pipelines,
    write_model_comparison_report,
)


CLEANED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "telco_customer_churn_cleaned.csv"
REPORT_PATH = PROJECT_ROOT / "reports" / "model_training_summary.md"
COMPARISON_CSV_PATH = PROJECT_ROOT / "reports" / "model_comparison.csv"


def main() -> None:
    """Run Phase 06 baseline model training."""
    data = pd.read_csv(CLEANED_DATA_PATH)
    split = create_train_test_split(data)

    comparison = compare_baseline_models(split.X_train, split.y_train)
    fitted_pipelines = fit_baseline_pipelines(split.X_train, split.y_train)

    comparison.to_csv(COMPARISON_CSV_PATH, index=False)
    write_model_comparison_report(comparison, REPORT_PATH)

    print(f"Cleaned dataset: {CLEANED_DATA_PATH}")
    print(f"Target column: {TARGET_COLUMN}")
    print(f"Excluded ID column: {ID_COLUMN}")
    print(f"Train shape: {split.X_train.shape}")
    print(f"Test shape: {split.X_test.shape}")
    print(f"Train churn rate: {split.y_train.mean():.4f}")
    print(f"Test churn rate: {split.y_test.mean():.4f}")
    print(f"Models trained: {', '.join(fitted_pipelines.keys())}")
    print(f"Comparison CSV: {COMPARISON_CSV_PATH}")
    print(f"Training summary: {REPORT_PATH}")
    print(comparison.round(4).to_string(index=False))


if __name__ == "__main__":
    main()
