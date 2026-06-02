# Exploratory Data Analysis Summary

## Scope

This summary documents Phase 04 exploratory analysis for the cleaned Telco Customer Churn dataset.

The analysis uses:

```text
data/processed/telco_customer_churn_cleaned.csv
```

No model training, feature preprocessing pipeline, or prediction code was created in this phase.

## Dataset Snapshot

- Rows: 7,043
- Columns: 21
- Target: `Churn`
- Target values: `0` for no churn, `1` for churn
- Missing values after Phase 03 cleaning: 0
- `TotalCharges` type after cleaning: numeric

## Target Distribution

- No churn customers: 5,174
- Churn customers: 1,869
- Overall churn rate: 26.5%

The target is not evenly balanced. Future model evaluation should avoid relying only on accuracy and should include recall, precision, F1-score, ROC-AUC, and confusion matrix.

## Numerical Insights

Average values by churn status:

| Churn | tenure | MonthlyCharges | TotalCharges |
| --- | ---: | ---: | ---: |
| No churn | 37.57 | 61.27 | 2549.91 |
| Churn | 17.98 | 74.44 | 1531.80 |

Key observations:

- Churned customers have much lower average tenure.
- Churned customers have higher average monthly charges.
- Churned customers have lower total charges mostly because they tend to leave earlier.

## Tenure Pattern

Churn rate by tenure group:

| Tenure group | Churn rate |
| --- | ---: |
| 0-12 months | 47.4% |
| 13-24 months | 28.7% |
| 25-48 months | 20.4% |
| 49-72 months | 9.5% |

The first year is the highest-risk customer lifecycle period. Early retention actions may have the most business value.

## Categorical Insights

Selected churn rates:

| Feature | Highest-risk segment | Churn rate |
| --- | --- | ---: |
| Contract | Month-to-month | 42.7% |
| InternetService | Fiber optic | 41.9% |
| PaymentMethod | Electronic check | 45.3% |
| SeniorCitizen | Senior citizen | 41.7% |
| Partner | No partner | 33.0% |
| Dependents | No dependents | 31.3% |

Additional observations:

- Gender has very little separation between churn rates.
- Contract type appears highly important for churn behavior.
- Electronic check customers show elevated churn risk.
- Fiber optic customers show higher churn than DSL or no internet service.
- Customers without partners or dependents show higher churn rates.

## Saved Figures

The notebook saves the following figures:

- `reports/figures/churn_distribution.png`
- `reports/figures/numeric_variables_by_churn.png`
- `reports/figures/tenure_group_churn_rate.png`
- `reports/figures/categorical_churn_rates.png`

## Business Takeaways

- The project should treat churn as a meaningful minority class.
- Retention efforts may be most useful during the first 12 months.
- Month-to-month contract customers should be considered a priority segment.
- Fiber optic and electronic check customers deserve deeper investigation.
- Later modeling should test whether tenure, contract type, monthly charges, internet service, and payment method are strong predictors.

## Recommended Next Phase

Phase 05 should build preprocessing and feature engineering logic for modeling. It should separate the target from features, preserve `customerID` only for traceability, encode categorical variables, scale numeric variables where appropriate, and prepare a train/test split.
