"""Prepare the Telco Customer Churn dataset for later project phases."""

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.data.clean_data import clean_telco_churn_data
from src.data.load_data import RAW_DATA_PATH, load_raw_telco_churn


PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "telco_customer_churn_cleaned.csv"


def main() -> None:
    """Run the raw-to-processed data cleaning workflow."""
    raw_data = load_raw_telco_churn(RAW_DATA_PATH)
    cleaned_data, report = clean_telco_churn_data(raw_data)

    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    cleaned_data.to_csv(PROCESSED_DATA_PATH, index=False)

    print(f"Raw dataset: {RAW_DATA_PATH}")
    print(f"Processed dataset: {PROCESSED_DATA_PATH}")
    print(f"Initial rows: {report.initial_rows}")
    print(f"Final rows: {report.final_rows}")
    print(f"Duplicate rows removed: {report.duplicate_rows_removed}")
    print(f"TotalCharges filled with zero: {report.total_charges_filled_with_zero}")
    print(f"Invalid TotalCharges rows removed: {report.total_charges_invalid_rows_removed}")
    print(f"Missing values after cleaning: {report.missing_values_after_cleaning}")


if __name__ == "__main__":
    main()
