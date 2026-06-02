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

The Phase 03 cleaning workflow creates this local processed file:

```text
data/processed/telco_customer_churn_cleaned.csv
```

This processed file is also ignored by Git.

The Phase 05 preprocessing workflow can also create local feature artifacts under:

```text
data/processed/features/
```

These files are ignored by Git and should be regenerated locally when needed.

## Raw-to-Processed Workflow

After placing the raw CSV at `data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv`, run:

```bash
python scripts/prepare_data.py
```

The script:

- Loads the raw Telco Customer Churn CSV.
- Validates required columns.
- Removes fully duplicated rows.
- Converts `TotalCharges` to numeric.
- Fills blank `TotalCharges` values with `0.0` when `tenure == 0`.
- Removes rows with invalid `TotalCharges` values that cannot be explained by zero tenure.
- Converts `Churn` from `Yes` / `No` into `1` / `0`.
- Saves the cleaned CSV locally under `data/processed/`.

`customerID` is preserved for traceability, but it should not be used as a modeling feature in later phases.

## Feature Preprocessing Workflow

After creating `data/processed/telco_customer_churn_cleaned.csv`, run:

```bash
python scripts/prepare_features.py
```

The script:

- Loads the cleaned dataset.
- Separates `Churn` as the target.
- Excludes `customerID` from modeling features.
- Creates a reproducible stratified train/test split.
- Fits the preprocessing pipeline only on the training features.
- Transforms train and test features separately.
- Saves local feature artifacts under `data/processed/features/`.

The preprocessing pipeline uses median imputation and scaling for numeric columns, plus most-frequent imputation and one-hot encoding for categorical columns.

## Current Status

The raw dataset and cleaned dataset can exist locally, but both remain ignored by Git.
