"""Run project quality checks that do not require local datasets."""

from pathlib import Path
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]

EXPECTED_TRACKED_FILES = [
    "README.md",
    "roadmap.md",
    "data/README.md",
    "docs/dataset_context.md",
    "reports/eda_summary.md",
    "reports/model_training_summary.md",
    "reports/model_evaluation_summary.md",
    "reports/model_interpretation.md",
    "reports/business_recommendations.md",
    "reports/final_project_summary.md",
    "scripts/prepare_data.py",
    "scripts/prepare_features.py",
    "scripts/train_baselines.py",
    "scripts/evaluate_model.py",
    "scripts/run_checks.py",
]


def check_expected_files() -> list[str]:
    """Return expected tracked files that are missing."""
    return [
        relative_path
        for relative_path in EXPECTED_TRACKED_FILES
        if not (PROJECT_ROOT / relative_path).exists()
    ]


def run_unittest_suite() -> int:
    """Run the unittest test suite."""
    command = [
        sys.executable,
        "-m",
        "unittest",
        "discover",
        "-s",
        "tests",
        "-p",
        "test_*.py",
    ]
    completed = subprocess.run(command, cwd=PROJECT_ROOT, check=False)
    return completed.returncode


def main() -> int:
    """Run project validation checks."""
    missing_files = check_expected_files()
    if missing_files:
        print("Missing expected files:")
        for missing_file in missing_files:
            print(f"- {missing_file}")
        return 1

    print("Expected tracked files: OK")
    test_status = run_unittest_suite()
    if test_status != 0:
        return test_status

    print("Unit tests: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
