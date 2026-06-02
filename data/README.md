# Data

This project is planned around the Telco Customer Churn dataset.

## Raw Data

Raw data should be placed in `data/raw/` after it is downloaded by the user. The raw dataset is intentionally not committed to this repository.

Recommended source:

- Telco Customer Churn dataset from Kaggle / IBM sample references.

Suggested local file location after download:

```text
data/raw/Telco-Customer-Churn.csv
```

If the downloaded file has a different name, keep it inside `data/raw/` and update later notebooks or scripts accordingly.

## Git Policy

Raw data should not be committed to Git. The `.gitignore` file excludes files inside `data/raw/` and `data/processed/` while keeping `.gitkeep` placeholders so the folder structure remains visible.

Do not commit:

- Raw datasets.
- Private customer data.
- Files with unclear license permissions.
- Generated processed data unless it is confirmed safe to share.

## Expected Target

- `Churn`: customer churn indicator, usually represented as `Yes` / `No`.

Later phases may encode this target as `1` for churn and `0` for no churn.

## Expected Columns

The dataset is expected to include customer identity, demographics, account information, services, billing values, and the churn target.

Examples:

- `customerID`
- `gender`
- `SeniorCitizen`
- `Partner`
- `Dependents`
- `tenure`
- `PhoneService`
- `InternetService`
- `Contract`
- `PaymentMethod`
- `MonthlyCharges`
- `TotalCharges`
- `Churn`

## Modeling Goal

The project will use the dataset to train a binary classification model that predicts customer churn risk. Later phases should evaluate the model with classification metrics such as accuracy, precision, recall, F1-score, ROC-AUC, and a confusion matrix.

For churn detection, recall for the churn class is especially important because the business wants to identify as many at-risk customers as possible.

## Processed Data

Processed files, when created in later phases, should be placed in `data/processed/`. They should only be committed if the license and privacy constraints are clear.

## Current Status

No dataset has been downloaded or added in Phase 02.
