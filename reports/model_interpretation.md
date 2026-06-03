# Model Interpretation

## Scope

This report documents Phase 08 model interpretation for the selected baseline model:

```text
LogisticRegression(class_weight="balanced")
```

The model was selected in Phase 06 based on training cross-validation and evaluated once on the held-out test set in Phase 07. This phase does not retrain models for selection, tune hyperparameters, optimize thresholds, or change the selected model.

## Held-out Performance Summary

| Metric | Value |
| --- | ---: |
| Accuracy | 0.7381 |
| Precision | 0.5043 |
| Recall | 0.7834 |
| F1 score | 0.6136 |
| ROC-AUC | 0.8416 |

The model shows strong recall for churn detection. It identified most customers who churned in the held-out test set, while accepting a meaningful number of false positives.

## Confusion Matrix Interpretation

| Actual / Predicted | No churn | Churn |
| --- | ---: | ---: |
| No churn | 747 | 288 |
| Churn | 81 | 293 |

Interpretation:

- True negatives: 747 customers did not churn and were correctly predicted as no churn.
- False positives: 288 customers did not churn but were flagged as churn risk.
- False negatives: 81 customers churned but were not flagged.
- True positives: 293 customers churned and were correctly flagged.

For churn detection, false negatives are the main business risk. A false negative is a customer who actually leaves but is not flagged for retention. The model missed 81 churn customers in the held-out test set.

False positives also matter because they can create unnecessary retention outreach. However, in many retention contexts, false positives may be acceptable if the cost of outreach is lower than the cost of losing a customer.

## Recall and ROC-AUC in Churn Terms

Recall of 0.7834 means the model caught about 78% of actual churn customers in the held-out test set. This is useful for a retention workflow because the business usually wants to find as many at-risk customers as possible before they leave.

ROC-AUC of 0.8416 means the model has strong ability to rank churn risk. In practical terms, customers with higher predicted churn probabilities are generally more likely to churn than customers with lower predicted probabilities.

The current model uses the default classification threshold of 0.5. Threshold tradeoffs can be discussed conceptually, but this project does not optimize the threshold on the held-out test set.

## Coefficient-Based Interpretation

The figure below summarizes the largest logistic regression coefficients by absolute value:

```text
reports/figures/logistic_regression_top_coefficients.png
```

Important caution: logistic regression coefficients show model associations after preprocessing. They do not prove causality. Correlated features can also affect coefficient direction and magnitude.

Positive coefficients are associated with higher predicted churn risk. Negative coefficients are associated with lower predicted churn risk.

High positive associations observed:

- Fiber optic internet service.
- Month-to-month contract.
- Electronic check payment method.
- No online security.
- No tech support.

High negative associations observed:

- Longer tenure.
- Two-year contract.
- DSL internet service.
- No internet service indicators.

The coefficient view mostly aligns with the EDA findings: churn risk is higher for month-to-month customers, fiber optic customers, electronic check customers, and customers with fewer support/security services.

## Metric Tradeoff

The model is oriented toward catching churn customers. That gives useful recall but produces false positives. This means a business team using the model should expect a retention list that includes some customers who would not have churned.

This tradeoff may be acceptable when:

- Retention outreach is inexpensive.
- The customer lifetime value is high.
- Missing churn customers is more costly than contacting extra customers.

This tradeoff may be less acceptable when:

- Retention offers are expensive.
- Outreach capacity is limited.
- False alarms create customer experience issues.

## Current Interpretation Summary

The model is a credible baseline for ranking churn risk and identifying many at-risk customers. It is not a final production system. Its best use at this stage is to support learning, portfolio demonstration, and business-oriented discussion of churn risk patterns.
