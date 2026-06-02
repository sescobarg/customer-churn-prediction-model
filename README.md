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
|-- src/
|   |-- data/
|-- models/
|-- reports/
|   |-- figures/
|-- tests/
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- roadmap.md
```

## Current Status

Phase 03 is complete. The project includes a reusable raw-to-processed data cleaning workflow for the Telco Customer Churn dataset.

No notebooks, exploratory charts, machine learning models, trained model artifacts, or model reports have been added yet.

## Next Step

Phase 04 will focus on exploratory data analysis.
