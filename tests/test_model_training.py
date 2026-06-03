import unittest

import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from src.features.build_features import (
    ID_COLUMN,
    TARGET_COLUMN,
    create_train_test_split,
)
from src.models.train_model import (
    BASELINE_SCORING,
    build_training_pipeline,
    compare_baseline_models,
    fit_baseline_pipelines,
)


class TestModelTraining(unittest.TestCase):
    def setUp(self) -> None:
        self.data = pd.DataFrame(
            {
                ID_COLUMN: [f"C{i:03d}" for i in range(80)],
                "tenure": list(range(80)),
                "MonthlyCharges": [20.0 + (i % 30) for i in range(80)],
                "TotalCharges": [100.0 + i * 8 for i in range(80)],
                "Contract": ["Month-to-month", "One year", "Two year", "Month-to-month"]
                * 20,
                "InternetService": ["Fiber optic", "DSL", "No", "DSL"] * 20,
                "PaymentMethod": [
                    "Electronic check",
                    "Mailed check",
                    "Bank transfer (automatic)",
                    "Credit card (automatic)",
                ]
                * 20,
                TARGET_COLUMN: [0, 1, 0, 1] * 20,
            }
        )
        self.split = create_train_test_split(self.data, test_size=0.25, random_state=42)

    def test_build_training_pipeline_contains_preprocessor_and_model(self) -> None:
        pipeline = build_training_pipeline(
            DummyClassifier(strategy="most_frequent"),
            self.split.X_train,
        )

        self.assertIsInstance(pipeline, Pipeline)
        self.assertEqual(list(pipeline.named_steps), ["preprocessor", "model"])
        self.assertFalse(hasattr(pipeline.named_steps["preprocessor"], "transformers_"))

    def test_compare_baseline_models_returns_cross_validation_metrics(self) -> None:
        models = {
            "dummy": DummyClassifier(strategy="most_frequent"),
            "logistic": LogisticRegression(max_iter=1000, class_weight="balanced"),
        }

        results = compare_baseline_models(
            self.split.X_train,
            self.split.y_train,
            models=models,
            cv_splits=3,
        )

        self.assertEqual(set(results["model"]), {"dummy", "logistic"})
        for metric_name in BASELINE_SCORING:
            self.assertIn(f"{metric_name}_mean", results.columns)
            self.assertIn(f"{metric_name}_std", results.columns)
        self.assertTrue(results["roc_auc_mean"].between(0, 1).all())

    def test_fit_baseline_pipelines_fits_preprocessing_inside_pipeline(self) -> None:
        models = {"dummy": DummyClassifier(strategy="most_frequent")}

        fitted = fit_baseline_pipelines(self.split.X_train, self.split.y_train, models=models)
        pipeline = fitted["dummy"]

        self.assertTrue(hasattr(pipeline.named_steps["preprocessor"], "transformers_"))
        self.assertNotIn(ID_COLUMN, self.split.X_train.columns)
        self.assertNotIn(TARGET_COLUMN, self.split.X_train.columns)


if __name__ == "__main__":
    unittest.main()
