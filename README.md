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
|   |-- train_baselines.py
|-- src/
|   |-- data/
|   |-- features/
|   |-- models/
|-- models/
|-- reports/
|   |-- figures/
|   |-- eda_summary.md
|   |-- model_training_summary.md
|-- tests/
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- roadmap.md
```

## Current Status

Phase 06 is complete. The project includes baseline model training with full scikit-learn pipelines and cross-validation on the training split.

No final model evaluation, prediction code, deployment, or final business conclusions have been added yet.

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

## Next Step

Phase 07 will focus on held-out model evaluation.
