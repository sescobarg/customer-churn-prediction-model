"""Data loading helpers for the Telco Customer Churn dataset."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"


def load_raw_telco_churn(path: str | Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Load the raw Telco Customer Churn CSV.

    Args:
        path: Local path to the raw CSV file.

    Returns:
        A pandas DataFrame with the raw dataset.

    Raises:
        FileNotFoundError: If the raw CSV does not exist.
        ValueError: If the provided file is not a CSV file.
    """
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Raw dataset not found: {csv_path}")
    if csv_path.suffix.lower() != ".csv":
        raise ValueError(f"Expected a CSV file, got: {csv_path}")

    return pd.read_csv(csv_path)
