# Project Roadmap

This project will be implemented incrementally. Each phase should be validated before moving to the next one.

## Phase 01 - Project Initialization [Complete]

- Create the base repository structure.
- Add initial documentation.
- Add `requirements.txt` and `.gitignore`.
- Keep empty folders with `.gitkeep`.

## Phase 02 - Dataset and Business Context [Complete]

- Document the Telco Customer Churn dataset source.
- Define the target variable and expected columns.
- Establish basic success criteria for the churn prediction task.
- Document raw data placement and Git data handling rules.

## Phase 03 - Data Cleaning [Complete]

- Inspect missing values, duplicates, and data types.
- Handle `TotalCharges` conversion.
- Prepare reusable cleaning logic in `src/`.
- Add a preparation script that saves the cleaned dataset locally.
- Add basic tests for cleaning behavior.

## Phase 04 - Exploratory Data Analysis [Complete]

- Analyze churn distribution.
- Explore numeric and categorical relationships.
- Save relevant figures under `reports/figures/`.
- Add a notebook with business-oriented EDA insights.
- Add an EDA summary report.

## Phase 05 - Preprocessing and Feature Engineering [Complete]

- Split features and target.
- Build a reproducible preprocessing pipeline.
- Prepare encoded and scaled features for training.
- Exclude `customerID` from modeling features.
- Fit preprocessing only on train data and transform test data separately.
- Add tests for feature/target separation and preprocessing behavior.

## Phase 06 - Model Training [Complete]

- Train baseline and tree-based classification models.
- Compare initial model performance.
- Use full scikit-learn pipelines with preprocessing and estimators.
- Compare baselines with cross-validation on the training split.
- Add a model training summary and comparison table.

## Phase 07 - Model Evaluation [Complete]

- Evaluate accuracy, precision, recall, F1-score, ROC-AUC, and confusion matrix.
- Document results in a model report.
- Evaluate the selected baseline once on the held-out test set.
- Generate confusion matrix, ROC curve, and precision-recall curve figures.
- Add reusable model evaluation logic and tests.

## Phase 08 - Interpretation and Business Conclusions [Complete]

- Explain relevant churn drivers.
- Document limitations and retention recommendations.
- Interpret held-out test metrics in churn business terms.
- Explain false positives, false negatives, recall, and ROC-AUC.
- Add model interpretation and business recommendation reports.

## Phase 09 - Basic Testing [Complete]

- Add tests for cleaning, loading, preprocessing, training, evaluation, report generation, and expected columns.
- Add a lightweight validation script for tracked project checks.
- Confirm data, feature artifacts, virtual environments, and model binaries stay out of Git.

## Phase 10 - Portfolio Polish [Complete]

- Review documentation, notebooks, code, and repository consistency.
- Prepare the project for GitHub portfolio presentation.
- Polish the README for portfolio review.
- Add a final project summary.
- Validate tests, reports, figures, ignored data files, and Git status.

## Final Checklist

- All phases from 01 through 10 are complete.
- Raw data, processed data, feature artifacts, virtual environments, caches, and model binaries are not committed.
- README describes the business problem, methodology, commands, results, limitations, and next steps.
- Reports include EDA, baseline training, held-out evaluation, interpretation, recommendations, and final summary.
- Validation passes with `python scripts/run_checks.py`.
