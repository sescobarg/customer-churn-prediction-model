# Data

This project is planned around the Telco Customer Churn dataset.

## Raw Data

Raw data should be placed in `data/raw/` after it is downloaded by the user. The raw dataset is intentionally not committed to the repository during the setup phase.

Recommended source:

- Telco Customer Churn dataset from Kaggle / IBM sample references.

## Expected Target

- `Churn`: customer churn indicator, usually represented as `Yes` / `No`.

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

## Processed Data

Processed files, when created in later phases, should be placed in `data/processed/`. They should only be committed if the license and privacy constraints are clear.

## Current Status

No dataset has been downloaded or added in Phase 01.
