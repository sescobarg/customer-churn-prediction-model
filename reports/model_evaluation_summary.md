# Held-out Model Evaluation Summary

## Scope

This report documents Phase 07 held-out test evaluation. The selected baseline model is fit on the training split only and evaluated once on the held-out test set.

No hyperparameters or thresholds are tuned on the held-out test set.

## Selected Model

- `logistic_regression`
- Full pipeline: preprocessing + classifier
- Classification threshold: default `0.5`

## Held-out Test Metrics

- Accuracy: `0.7381`
- Precision: `0.5043`
- Recall: `0.7834`
- F1 score: `0.6136`
- ROC-AUC: `0.8416`

## Confusion Matrix

| Actual / Predicted | No churn | Churn |
| --- | ---: | ---: |
| No churn | 747 | 288 |
| Churn | 81 | 293 |

For churn detection, false negatives are customers who churned but were predicted as no churn. These are especially costly because the business may miss the opportunity to intervene.

- False negatives: `81`
- True positives: `293`

Recall measures how many actual churn customers the model caught. ROC-AUC measures how well the model ranks churn risk across thresholds, without choosing a custom threshold on the test set.

## Classification Report

```text
precision    recall  f1-score   support

    No churn       0.90      0.72      0.80      1035
       Churn       0.50      0.78      0.61       374

    accuracy                           0.74      1409
   macro avg       0.70      0.75      0.71      1409
weighted avg       0.80      0.74      0.75      1409
```

## Generated Figures

- `reports/figures/confusion_matrix.png`
- `reports/figures/roc_curve.png`
- `reports/figures/precision_recall_curve.png`

## Status Note

Phase 08 added model interpretation, limitations, and business recommendations without retuning on the held-out test set.
