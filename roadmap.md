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

## Phase 06 - Model Training

- Train baseline and tree-based classification models.
- Compare initial model performance.

## Phase 07 - Model Evaluation

- Evaluate accuracy, precision, recall, F1-score, ROC-AUC, and confusion matrix.
- Document results in a model report.

## Phase 08 - Interpretation and Business Conclusions

- Explain relevant churn drivers.
- Document limitations and retention recommendations.

## Phase 09 - Basic Testing

- Add tests for cleaning, preprocessing, prediction, and expected columns.

## Phase 10 - Portfolio Polish

- Review documentation, notebooks, code, and repository consistency.
- Prepare the project for GitHub portfolio presentation.
