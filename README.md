# Customer Churn Prediction Model

Machine learning portfolio project focused on predicting customer churn for a telecom service.

## Project Overview

The goal is to build a clean, reproducible classification project that estimates whether a customer is at risk of leaving the service. The repository will be developed incrementally by phases, with notebooks for exploration and reusable logic inside `src/`.

## Business Problem

Telecom companies need to identify customers with a high probability of churn so retention actions can be prioritized before customers leave.

## Dataset

The planned dataset is the Telco Customer Churn dataset. Raw data is not included in this repository and should not be committed to Git. Download instructions and data handling notes are documented in `data/README.md`.

Additional business and dataset context is available in `docs/dataset_context.md`.

## Initial Scope

- Project structure and documentation.
- Dataset instructions.
- Future exploratory notebooks.
- Future reusable Python modules for cleaning, preprocessing, training, evaluation, and prediction.
- Future basic tests and validation checks.

## Technologies

- Python
- pandas
- NumPy
- matplotlib
- seaborn
- scikit-learn
- joblib
- pytest
- Jupyter Notebook

## Project Structure

```text
customer-churn-prediction-model/
|-- data/
|   |-- raw/
|   |-- processed/
|   |-- README.md
|-- docs/
|   |-- dataset_context.md
|-- notebooks/
|-- scripts/
|   |-- prepare_data.py
|   |-- prepare_features.py
|   |-- evaluate_model.py
|   |-- train_baselines.py
|-- src/
|   |-- data/
|   |-- features/
|   |-- models/
|-- models/
|-- reports/
|   |-- figures/
|   |-- business_recommendations.md
|   |-- eda_summary.md
|   |-- model_evaluation_summary.md
|   |-- model_interpretation.md
|   |-- model_training_summary.md
|-- tests/
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- roadmap.md
```

## Current Status

Phase 08 is complete. The project includes model interpretation, limitations, and business recommendations based on EDA, baseline training, and held-out evaluation.

No prediction code, deployment, API, app, or dashboard has been added yet.

## Key Findings

- The selected logistic regression baseline achieved held-out recall of `0.7834` and ROC-AUC of `0.8416`.
- The model caught `293` churn customers and missed `81` churn customers on the held-out test set.
- False negatives are the main business risk because they represent churn customers who would not be flagged for retention.
- False positives may be acceptable when retention outreach is less expensive than losing a customer.
- EDA and model interpretation point to risk indicators such as early tenure, month-to-month contracts, fiber optic service, electronic check payment, and limited support/security services.

Interpretation reports:

- `reports/model_interpretation.md`
- `reports/business_recommendations.md`

## How to Run

Prepare the cleaned dataset:

```bash
python scripts/prepare_data.py
```

Prepare local feature artifacts:

```bash
python scripts/prepare_features.py
```

Train and compare baseline models:

```bash
python scripts/train_baselines.py
```

Evaluate the selected baseline model on the held-out test set:

```bash
python scripts/evaluate_model.py
```

## Next Step

Phase 09 will focus on expanding basic tests and validation coverage.
