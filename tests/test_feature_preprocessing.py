import unittest

import pandas as pd

from src.features.build_features import (
    ID_COLUMN,
    TARGET_COLUMN,
    create_feature_target_split,
    create_train_test_split,
    fit_transform_train_test,
)


class TestFeaturePreprocessing(unittest.TestCase):
    def setUp(self) -> None:
        self.data = pd.DataFrame(
            {
                ID_COLUMN: [f"C{i:03d}" for i in range(40)],
                "tenure": list(range(40)),
                "MonthlyCharges": [20.0 + i for i in range(40)],
                "TotalCharges": [100.0 + i * 10 for i in range(40)],
                "Contract": ["Month-to-month", "One year"] * 20,
                "InternetService": ["Fiber optic", "DSL", "No", "DSL"] * 10,
                TARGET_COLUMN: [0, 1] * 20,
            }
        )

    def test_create_feature_target_split_excludes_id_and_target(self) -> None:
        X, y = create_feature_target_split(self.data)

        self.assertNotIn(ID_COLUMN, X.columns)
        self.assertNotIn(TARGET_COLUMN, X.columns)
        self.assertEqual(y.name, TARGET_COLUMN)
        self.assertEqual(len(X), len(y))

    def test_create_train_test_split_uses_stratification(self) -> None:
        split = create_train_test_split(self.data, test_size=0.25, random_state=42)

        self.assertEqual(split.X_train.shape[0], 30)
        self.assertEqual(split.X_test.shape[0], 10)
        self.assertAlmostEqual(split.y_train.mean(), self.data[TARGET_COLUMN].mean(), places=2)
        self.assertAlmostEqual(split.y_test.mean(), self.data[TARGET_COLUMN].mean(), places=2)

    def test_fit_transform_train_test_excludes_unseen_categorical_leakage(self) -> None:
        split = create_train_test_split(self.data, test_size=0.25, random_state=42)
        processed = fit_transform_train_test(split)

        self.assertEqual(processed.X_train_processed.shape[0], split.X_train.shape[0])
        self.assertEqual(processed.X_test_processed.shape[0], split.X_test.shape[0])
        self.assertEqual(
            processed.X_train_processed.shape[1],
            processed.X_test_processed.shape[1],
        )
        self.assertFalse(any(ID_COLUMN in name for name in processed.feature_names))
        self.assertFalse(any(TARGET_COLUMN in name for name in processed.feature_names))
        self.assertGreater(len(processed.feature_names), split.X_train.shape[1])

    def test_missing_target_column_raises_error(self) -> None:
        data = self.data.drop(columns=[TARGET_COLUMN])

        with self.assertRaisesRegex(ValueError, "Missing target column"):
            create_feature_target_split(data)


if __name__ == "__main__":
    unittest.main()
