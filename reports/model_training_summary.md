# Baseline Model Training Summary

## Scope

This report documents Phase 06 baseline model training. It compares a small set of scikit-learn classifiers using stratified cross-validation on the training split only.

The held-out test set is not used for model selection in this phase. Final evaluation belongs to Phase 07.

## Models Compared

- `DummyClassifier(strategy="most_frequent")`
- `LogisticRegression(class_weight="balanced")`
- `RandomForestClassifier(class_weight="balanced")`

## Cross-Validation Results

| model | roc_auc_mean | roc_auc_std | accuracy_mean | accuracy_std | precision_mean | precision_std | recall_mean | recall_std | f1_mean | f1_std |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| logistic_regression | 0.846 | 0.0124 | 0.7485 | 0.0153 | 0.5169 | 0.0189 | 0.8013 | 0.0379 | 0.6283 | 0.0232 |
| random_forest | 0.8188 | 0.0103 | 0.787 | 0.0095 | 0.6313 | 0.022 | 0.4742 | 0.0296 | 0.5413 | 0.0249 |
| dummy_most_frequent | 0.5 | 0.0 | 0.7346 | 0.0001 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## Current Best Baseline

- Best ROC-AUC: `logistic_regression` with ROC-AUC `0.8460`.
- Recall for that model: `0.8013`.

Because churn detection cares about identifying at-risk customers, recall and ROC-AUC should remain important during Phase 07 evaluation.

## Next Step

Phase 07 should evaluate the selected candidate models on the held-out test set with classification metrics and confusion matrix.
