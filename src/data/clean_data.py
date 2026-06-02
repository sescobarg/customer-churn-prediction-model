"""Cleaning logic for the Telco Customer Churn dataset."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


REQUIRED_COLUMNS = {
    "customerID",
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
    "Churn",
}

TARGET_MAPPING = {
    "No": 0,
    "Yes": 1,
}


@dataclass(frozen=True)
class CleaningReport:
    """Summary of important cleaning decisions and checks."""

    initial_rows: int
    final_rows: int
    duplicate_rows_removed: int
    total_charges_filled_with_zero: int
    total_charges_invalid_rows_removed: int
    missing_values_after_cleaning: dict[str, int]


def validate_required_columns(data: pd.DataFrame) -> None:
    """Validate that the expected minimum columns exist."""
    missing_columns = sorted(REQUIRED_COLUMNS.difference(data.columns))
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")


def clean_telco_churn_data(data: pd.DataFrame) -> tuple[pd.DataFrame, CleaningReport]:
    """Clean the Telco Customer Churn dataset.

    Cleaning decisions:
    - Preserve `customerID` for traceability.
    - Remove fully duplicated rows.
    - Convert `TotalCharges` to numeric.
    - Treat blank `TotalCharges` values with `tenure == 0` as `0.0`.
    - Remove rows with invalid `TotalCharges` values that cannot be explained by
      zero tenure.
    - Convert `Churn` from `Yes`/`No` to binary `1`/`0`.
    """
    validate_required_columns(data)

    cleaned = data.copy()
    initial_rows = len(cleaned)

    duplicate_rows = int(cleaned.duplicated().sum())
    cleaned = cleaned.drop_duplicates().reset_index(drop=True)

    cleaned["TotalCharges"] = pd.to_numeric(cleaned["TotalCharges"], errors="coerce")
    missing_total_charges = cleaned["TotalCharges"].isna()
    zero_tenure_missing_total = missing_total_charges & (cleaned["tenure"] == 0)
    filled_with_zero = int(zero_tenure_missing_total.sum())
    cleaned.loc[zero_tenure_missing_total, "TotalCharges"] = 0.0

    invalid_total_charges = cleaned["TotalCharges"].isna()
    invalid_total_rows_removed = int(invalid_total_charges.sum())
    if invalid_total_rows_removed:
        cleaned = cleaned.loc[~invalid_total_charges].copy()

    cleaned["Churn"] = cleaned["Churn"].astype(str).str.strip()
    invalid_target = sorted(set(cleaned["Churn"].dropna()) - set(TARGET_MAPPING))
    if invalid_target:
        raise ValueError(f"Unexpected Churn values: {invalid_target}")
    cleaned["Churn"] = cleaned["Churn"].map(TARGET_MAPPING).astype("int64")

    cleaned = cleaned.reset_index(drop=True)
    missing_values = {
        column: int(count)
        for column, count in cleaned.isna().sum().items()
        if int(count) > 0
    }

    report = CleaningReport(
        initial_rows=initial_rows,
        final_rows=len(cleaned),
        duplicate_rows_removed=duplicate_rows,
        total_charges_filled_with_zero=filled_with_zero,
        total_charges_invalid_rows_removed=invalid_total_rows_removed,
        missing_values_after_cleaning=missing_values,
    )

    return cleaned, report
