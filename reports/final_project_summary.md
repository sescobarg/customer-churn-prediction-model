# Final Project Summary

## Overview

This project is a portfolio-ready baseline machine learning workflow for telecom customer churn prediction. It demonstrates a complete and reproducible process from dataset documentation through data cleaning, EDA, preprocessing, model training, held-out evaluation, interpretation, recommendations, and validation.

The project is not production-ready and does not include deployment, inference endpoints, monitoring, or automated retraining.

## Dataset

The project uses the Telco Customer Churn dataset. Raw and generated datasets are not committed to Git. The expected local raw file is:

```text
data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv
```

The cleaned local dataset produced by the project is:

```text
data/processed/telco_customer_churn_cleaned.csv
```

## Workflow

1. Document dataset and business context.
2. Clean the raw dataset and preserve `customerID` for traceability.
3. Explore churn patterns with EDA and saved figures.
4. Split features and target while excluding `customerID`.
5. Build preprocessing with numeric scaling and categorical one-hot encoding.
6. Compare baseline models with cross-validation on the training split.
7. Evaluate the selected model once on the held-out test set.
8. Interpret metrics, coefficients, business tradeoffs, and limitations.
9. Validate reusable code with tests and a project check script.
10. Polish documentation for portfolio presentation.

## Selected Model

The selected model is:

```text
LogisticRegression(class_weight="balanced")
```

It was selected from baseline cross-validation results on the training split and evaluated once on the held-out test set.

## Held-out Test Results

| Metric | Value |
| --- | ---: |
| Accuracy | 0.7381 |
| Precision | 0.5043 |
| Recall | 0.7834 |
| F1 score | 0.6136 |
| ROC-AUC | 0.8416 |

Confusion matrix:

| Actual / Predicted | No churn | Churn |
| --- | ---: | ---: |
| No churn | 747 | 288 |
| Churn | 81 | 293 |

The model catches many churn customers, which is useful for retention prioritization. The tradeoff is a meaningful number of false positives.

## Business Interpretation

Important churn risk indicators from EDA and model interpretation include:

- Early tenure.
- Month-to-month contracts.
- Fiber optic service.
- Electronic check payment.
- Lack of online security or tech support.
- Higher monthly charges in some customer segments.

These are risk indicators and model associations, not causal claims.

## Recommendations

- Prioritize outreach for early-tenure and month-to-month customers.
- Investigate fiber optic customer experience, billing friction, and support needs.
- Use churn scores to prioritize retention review rather than automate final decisions.
- Evaluate outreach costs against customer lifetime value before operational use.

## Limitations

- The dataset is sample-like and may not represent current real-world customer behavior.
- The model does not include operational signals such as complaints, outages, usage trends, or customer satisfaction.
- The threshold was not tuned.
- Coefficient interpretation is associative, not causal.
- No production deployment, monitoring, or feedback loop is included.

## Validation

Quality checks can be run with:

```bash
python scripts/run_checks.py
```

The final validation suite covers data loading, cleaning, preprocessing, model training helpers, evaluation helpers, report generation, and project file checks.
