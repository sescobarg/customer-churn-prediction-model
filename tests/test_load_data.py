import tempfile
import unittest
from pathlib import Path

import pandas as pd

from src.data.load_data import load_raw_telco_churn


class TestLoadData(unittest.TestCase):
    def test_load_raw_telco_churn_reads_csv(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "sample.csv"
            csv_path.write_text("customerID,Churn\nA,Yes\n", encoding="utf-8")

            data = load_raw_telco_churn(csv_path)

        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(data.shape, (1, 2))
        self.assertEqual(data.loc[0, "customerID"], "A")

    def test_load_raw_telco_churn_rejects_missing_file(self) -> None:
        with self.assertRaises(FileNotFoundError):
            load_raw_telco_churn("missing.csv")

    def test_load_raw_telco_churn_rejects_non_csv_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            text_path = Path(temp_dir) / "sample.txt"
            text_path.write_text("not csv", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "Expected a CSV file"):
                load_raw_telco_churn(text_path)


if __name__ == "__main__":
    unittest.main()
