# Dataset and Business Context

## Business Problem

Telecom companies operate with recurring customer relationships. When customers cancel or stop using the service, the business loses expected revenue and may need to spend more to acquire replacement customers.

The purpose of this project is to support customer retention by identifying customers with a higher probability of churn before they leave. These predictions can help prioritize retention campaigns, customer support actions, or service improvement efforts.

## Modeling Goal

Build a supervised binary classification model that predicts whether a telecom customer is likely to churn.

The model should eventually return:

- A churn prediction for each customer.
- A churn probability or risk score.
- Evaluation metrics that show how well the model identifies churn cases.

## Dataset Source

The planned dataset is the Telco Customer Churn dataset, commonly referenced through Kaggle and IBM sample materials.

Raw data is not included in this repository. Users should download the dataset separately and place it in `data/raw/`.

## Target Variable

The target variable is:

- `Churn`

Expected values:

- `Yes`: the customer churned.
- `No`: the customer did not churn.

During later phases, this target may be encoded as:

- `1`: churn.
- `0`: no churn.

## Expected Columns

The dataset is expected to include columns from these groups:

| Group | Example Columns |
| --- | --- |
| Customer identity | `customerID` |
| Demographics | `gender`, `SeniorCitizen`, `Partner`, `Dependents` |
| Account history | `tenure`, `Contract`, `PaperlessBilling`, `PaymentMethod` |
| Services | `PhoneService`, `InternetService`, `OnlineSecurity`, `TechSupport`, `StreamingTV`, `StreamingMovies` |
| Billing | `MonthlyCharges`, `TotalCharges` |
| Target | `Churn` |

## Success Criteria

This is a churn classification problem, so accuracy alone is not enough. Churn may be an imbalanced class, and the project should evaluate how well the model finds customers at risk.

Future model evaluation should include:

- Accuracy.
- Precision for churn.
- Recall for churn.
- F1-score.
- ROC-AUC.
- Confusion matrix.

Recall for churn will be especially important because missing a customer who is likely to leave can be costly for the business. Precision should also be monitored to avoid over-targeting customers who are not actually at risk.

## Data Handling Rules

- Do not commit raw data to Git.
- Do not commit private, sensitive, or licensed data without confirmation.
- Keep raw downloaded files in `data/raw/`.
- Keep processed datasets in `data/processed/` only when created in later phases.
- Commit only documentation, code, tests, and small safe artifacts unless data permissions are clear.

## Project Status Note

Dataset and business context were documented in Phase 02. Later phases added local data cleaning, EDA, preprocessing, baseline training, held-out evaluation, interpretation, and validation coverage.
