import tempfile
import unittest
from pathlib import Path

import pandas as pd
from sklearn.dummy import DummyClassifier

from src.features.build_features import create_train_test_split
from src.models.evaluate_model import evaluate_classifier, write_evaluation_report
from src.models.evaluate_model import (
    save_confusion_matrix_figure,
    save_precision_recall_curve_figure,
    save_roc_curve_figure,
)
from src.models.train_model import build_training_pipeline


class TestModelEvaluation(unittest.TestCase):
    def setUp(self) -> None:
        self.data = pd.DataFrame(
            {
                "customerID": [f"C{i:03d}" for i in range(40)],
                "tenure": list(range(40)),
                "MonthlyCharges": [20.0 + i for i in range(40)],
                "TotalCharges": [100.0 + i * 10 for i in range(40)],
                "Contract": ["Month-to-month", "One year"] * 20,
                "InternetService": ["Fiber optic", "DSL", "No", "DSL"] * 10,
                "Churn": [0, 1] * 20,
            }
        )
        self.split = create_train_test_split(self.data, test_size=0.25, random_state=42)

    def test_evaluate_classifier_returns_expected_metrics(self) -> None:
        pipeline = build_training_pipeline(
            DummyClassifier(strategy="stratified", random_state=42),
            self.split.X_train,
        )
        pipeline.fit(self.split.X_train, self.split.y_train)

        metrics = evaluate_classifier(pipeline, self.split.X_test, self.split.y_test)

        for key in ["accuracy", "precision", "recall", "f1", "roc_auc"]:
            self.assertIn(key, metrics)
            self.assertGreaterEqual(metrics[key], 0.0)
            self.assertLessEqual(metrics[key], 1.0)
        self.assertEqual(metrics["confusion_matrix"].shape, (2, 2))
        self.assertIn("No churn", metrics["classification_report"])
        self.assertIn("Churn", metrics["classification_report"])

    def test_write_evaluation_report_creates_markdown_file(self) -> None:
        pipeline = build_training_pipeline(
            DummyClassifier(strategy="stratified", random_state=42),
            self.split.X_train,
        )
        pipeline.fit(self.split.X_train, self.split.y_train)
        metrics = evaluate_classifier(pipeline, self.split.X_test, self.split.y_test)

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "evaluation.md"
            write_evaluation_report(metrics, output_path, "dummy")
            content = output_path.read_text(encoding="utf-8")

        self.assertIn("Held-out Model Evaluation Summary", content)
        self.assertIn("False negatives", content)
        self.assertIn("ROC-AUC", content)

    def test_evaluation_figure_helpers_create_files(self) -> None:
        pipeline = build_training_pipeline(
            DummyClassifier(strategy="stratified", random_state=42),
            self.split.X_train,
        )
        pipeline.fit(self.split.X_train, self.split.y_train)
        metrics = evaluate_classifier(pipeline, self.split.X_test, self.split.y_test)

        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            confusion_path = output_dir / "confusion.png"
            roc_path = output_dir / "roc.png"
            pr_path = output_dir / "precision_recall.png"

            save_confusion_matrix_figure(metrics["confusion_matrix"], confusion_path)
            save_roc_curve_figure(pipeline, self.split.X_test, self.split.y_test, roc_path)
            save_precision_recall_curve_figure(
                self.split.y_test,
                metrics["y_score"],
                pr_path,
            )

            self.assertTrue(confusion_path.exists())
            self.assertTrue(roc_path.exists())
            self.assertTrue(pr_path.exists())


if __name__ == "__main__":
    unittest.main()
