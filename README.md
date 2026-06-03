# Customer Churn Prediction Model

Portfolio-ready machine learning project for predicting telecom customer churn with Python, pandas, and scikit-learn.

## Project Goal

The goal is to build a reproducible churn prediction workflow that estimates whether a telecom customer is at risk of leaving the service. The project demonstrates practical work across data preparation, exploratory analysis, preprocessing, baseline modeling, held-out evaluation, interpretation, documentation, and validation.

This is a portfolio baseline project, not a production-ready churn system.

## Business Problem

Telecom companies lose revenue when customers cancel or stop using their service. A churn model can help prioritize customers for retention review before they leave.

For this use case, recall is especially important because false negatives are customers who actually churn but are not flagged for outreach.

## Dataset

The project uses the Telco Customer Churn dataset, commonly referenced through Kaggle and IBM sample materials.

Raw and generated data are intentionally not committed to Git:

- Raw CSV files stay under `data/raw/`.
- Cleaned datasets and feature artifacts stay under `data/processed/`.
- Model binaries stay under `models/` if created locally.
- `.gitkeep` files preserve the folder structure.

Expected raw file path:

```text
data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv
```

More details are in [data/README.md](data/README.md) and [docs/dataset_context.md](docs/dataset_context.md).

## Results at a Glance

Selected model:

```text
LogisticRegression(class_weight="balanced")
```

Held-out test metrics:

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

The model caught 293 churn customers and missed 81 churn customers on the held-out test set. It favors recall, which is useful for churn detection, while accepting more false positives.

## Key Findings

- Overall churn rate is about 26.5%.
- Churn is highest in the first 12 months of tenure.
- Month-to-month contracts show higher churn risk.
- Fiber optic service and electronic check payment are associated with elevated churn risk.
- Customers without online security or tech support appear more exposed to churn risk.
- Logistic regression coefficients align with EDA patterns, but they show associations, not causal effects.

## Methodology by Phase

| Phase | Focus | Main Output |
| --- | --- | --- |
| 01 | Project setup | Base structure, README, `.gitignore`, requirements |
| 02 | Dataset and business context | Dataset context and data handling rules |
| 03 | Data cleaning | Reusable cleaning pipeline and cleaned local CSV |
| 04 | EDA | Notebook, figures, and EDA summary |
| 05 | Preprocessing | Train/test split and sklearn preprocessing pipeline |
| 06 | Baseline training | Cross-validation comparison for baseline models |
| 07 | Held-out evaluation | Metrics, confusion matrix, ROC and PR curves |
| 08 | Interpretation | Model interpretation and business recommendations |
| 09 | Validation coverage | Expanded unittest suite and `run_checks.py` |
| 10 | Portfolio polish | Final README, roadmap, and project summary |

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
|   |-- 03_exploratory_data_analysis.ipynb
|-- scripts/
|   |-- prepare_data.py
|   |-- prepare_features.py
|   |-- train_baselines.py
|   |-- evaluate_model.py
|   |-- run_checks.py
|-- src/
|   |-- data/
|   |-- features/
|   |-- models/
|-- models/
|-- reports/
|   |-- figures/
|   |-- business_recommendations.md
|   |-- eda_summary.md
|   |-- final_project_summary.md
|   |-- model_evaluation_summary.md
|   |-- model_interpretation.md
|   |-- model_training_summary.md
|-- tests/
|-- requirements.txt
|-- roadmap.md
```

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

Place the raw dataset at:

```text
data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv
```

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

Run project quality checks:

```bash
python scripts/run_checks.py
```

## Reports

- [EDA summary](reports/eda_summary.md)
- [Baseline training summary](reports/model_training_summary.md)
- [Held-out evaluation summary](reports/model_evaluation_summary.md)
- [Model interpretation](reports/model_interpretation.md)
- [Business recommendations](reports/business_recommendations.md)
- [Final project summary](reports/final_project_summary.md)

## Business Interpretation

The selected model is useful as a churn-risk prioritization baseline. Its high recall means it catches many customers who churn, which is valuable when missed churn customers are more costly than extra outreach.

The tradeoff is that the model also produces false positives. These are customers who may receive retention outreach even though they would not have churned. That may be acceptable when outreach is low cost, but it should be evaluated against retention budget, customer lifetime value, and outreach capacity.

## Limitations

- The dataset is sample-like and may not represent a real company's current customers.
- The model does not include support tickets, outages, usage trends, customer satisfaction, or customer lifetime value.
- Logistic regression coefficients are associations, not causal explanations.
- The default threshold was used; no threshold tuning was performed on the held-out test set.
- The project does not include deployment, monitoring, inference endpoints, or an operational feedback loop.

## Possible Future Improvements

- Add cost-sensitive threshold analysis using a validation set and business cost assumptions.
- Add richer customer behavior and support interaction features.
- Compare more models or calibration strategies while preserving a clean validation design.
- Add model monitoring or retraining workflow if adapted to a real business setting.
- Build a lightweight API or dashboard only after the modeling workflow is stable.
