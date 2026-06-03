import unittest

import pandas as pd

from src.data.clean_data import clean_telco_churn_data, validate_required_columns


class TestDataCleaning(unittest.TestCase):
    def test_clean_telco_churn_data_converts_total_charges_and_target(self) -> None:
        raw_data = pd.DataFrame(
            {
                "customerID": ["A", "B", "C"],
                "tenure": [1, 0, 2],
                "MonthlyCharges": [29.85, 0.0, 40.0],
                "TotalCharges": ["29.85", " ", "80.0"],
                "Churn": ["No", "No", "Yes"],
            }
        )

        cleaned, report = clean_telco_churn_data(raw_data)

        self.assertEqual(len(cleaned), 3)
        self.assertIn(cleaned["TotalCharges"].dtype.kind, {"f", "i"})
        self.assertEqual(
            cleaned.loc[cleaned["customerID"] == "B", "TotalCharges"].iloc[0],
            0.0,
        )
        self.assertEqual(set(cleaned["Churn"].unique()), {0, 1})
        self.assertEqual(report.total_charges_filled_with_zero, 1)
        self.assertEqual(report.total_charges_invalid_rows_removed, 0)

    def test_clean_telco_churn_data_removes_unexplained_invalid_total_charges(
        self,
    ) -> None:
        raw_data = pd.DataFrame(
            {
                "customerID": ["A", "B"],
                "tenure": [3, 4],
                "MonthlyCharges": [29.85, 40.0],
                "TotalCharges": ["bad-value", "160.0"],
                "Churn": ["No", "Yes"],
            }
        )

        cleaned, report = clean_telco_churn_data(raw_data)

        self.assertEqual(list(cleaned["customerID"]), ["B"])
        self.assertEqual(report.total_charges_invalid_rows_removed, 1)

    def test_clean_telco_churn_data_removes_duplicate_rows(self) -> None:
        raw_data = pd.DataFrame(
            {
                "customerID": ["A", "A"],
                "tenure": [1, 1],
                "MonthlyCharges": [29.85, 29.85],
                "TotalCharges": ["29.85", "29.85"],
                "Churn": ["No", "No"],
            }
        )

        cleaned, report = clean_telco_churn_data(raw_data)

        self.assertEqual(len(cleaned), 1)
        self.assertEqual(report.duplicate_rows_removed, 1)

    def test_validate_required_columns_rejects_missing_columns(self) -> None:
        raw_data = pd.DataFrame({"customerID": ["A"]})

        with self.assertRaisesRegex(ValueError, "Missing required columns"):
            validate_required_columns(raw_data)

    def test_clean_telco_churn_data_rejects_unexpected_target_values(self) -> None:
        raw_data = pd.DataFrame(
            {
                "customerID": ["A"],
                "tenure": [1],
                "MonthlyCharges": [29.85],
                "TotalCharges": ["29.85"],
                "Churn": ["Maybe"],
            }
        )

        with self.assertRaisesRegex(ValueError, "Unexpected Churn values"):
            clean_telco_churn_data(raw_data)

    def test_clean_telco_churn_data_reports_remaining_missing_values(self) -> None:
        raw_data = pd.DataFrame(
            {
                "customerID": ["A"],
                "tenure": [1],
                "MonthlyCharges": [None],
                "TotalCharges": ["29.85"],
                "Churn": ["No"],
            }
        )

        _, report = clean_telco_churn_data(raw_data)

        self.assertEqual(report.missing_values_after_cleaning, {"MonthlyCharges": 1})


if __name__ == "__main__":
    unittest.main()
