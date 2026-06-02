"""Prepare model-ready train/test feature matrices for later modeling phases."""

from pathlib import Path
import sys

import joblib


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.data.load_data import load_raw_telco_churn
from src.features.build_features import (
    ID_COLUMN,
    TARGET_COLUMN,
    create_train_test_split,
    fit_transform_train_test,
    get_matrix_shape,
)


CLEANED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "telco_customer_churn_cleaned.csv"
FEATURE_OUTPUT_DIR = PROJECT_ROOT / "data" / "processed" / "features"


def main() -> None:
    """Run the Phase 05 preprocessing workflow."""
    data = load_raw_telco_churn(CLEANED_DATA_PATH)
    split = create_train_test_split(data)
    processed = fit_transform_train_test(split)

    FEATURE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(processed.X_train_processed, FEATURE_OUTPUT_DIR / "X_train_processed.joblib")
    joblib.dump(processed.X_test_processed, FEATURE_OUTPUT_DIR / "X_test_processed.joblib")
    joblib.dump(processed.y_train, FEATURE_OUTPUT_DIR / "y_train.joblib")
    joblib.dump(processed.y_test, FEATURE_OUTPUT_DIR / "y_test.joblib")
    joblib.dump(processed.preprocessor, FEATURE_OUTPUT_DIR / "preprocessor.joblib")
    joblib.dump(processed.feature_names, FEATURE_OUTPUT_DIR / "feature_names.joblib")

    train_churn_rate = split.y_train.mean()
    test_churn_rate = split.y_test.mean()

    print(f"Cleaned dataset: {CLEANED_DATA_PATH}")
    print(f"Target column: {TARGET_COLUMN}")
    print(f"Excluded ID column: {ID_COLUMN}")
    print(f"Train rows: {len(split.X_train)}")
    print(f"Test rows: {len(split.X_test)}")
    print(f"Train churn rate: {train_churn_rate:.4f}")
    print(f"Test churn rate: {test_churn_rate:.4f}")
    print(f"Processed train shape: {get_matrix_shape(processed.X_train_processed)}")
    print(f"Processed test shape: {get_matrix_shape(processed.X_test_processed)}")
    print(f"Processed feature count: {len(processed.feature_names)}")
    print(f"Feature artifacts directory: {FEATURE_OUTPUT_DIR}")


if __name__ == "__main__":
    main()
