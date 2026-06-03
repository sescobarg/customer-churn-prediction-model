# Business Recommendations

## Scope

This report translates the EDA and held-out model evaluation into practical retention recommendations. It does not introduce new model tuning, threshold optimization, deployment logic, or prediction tooling.

## Key Business Findings

The project found several recurring churn risk signals:

- Overall churn rate is about 26.5%.
- Customers in the first 12 months have the highest churn rate.
- Month-to-month contracts show much higher churn than one-year and two-year contracts.
- Fiber optic customers show elevated churn.
- Electronic check customers show elevated churn.
- Customers without online security or tech support appear more exposed to churn risk.
- The selected model achieved strong recall on the held-out test set, catching 293 churn customers while missing 81.

These findings should be treated as risk indicators, not causal proof.

## Recommended Retention Actions

### 1. Prioritize Early-Tenure Customers

Customers in their first year showed the highest churn rate in the EDA. The business should consider onboarding, service-quality check-ins, and early satisfaction monitoring during this period.

Recommended actions:

- Create a first-90-day onboarding follow-up.
- Monitor new customer service issues closely.
- Offer proactive support before the first renewal or billing friction point.

### 2. Review Month-to-Month Contract Risk

Month-to-month contracts were a strong churn risk indicator in both EDA and model interpretation.

Recommended actions:

- Offer incentives for customers to move to annual or two-year contracts.
- Test non-disruptive loyalty benefits for month-to-month customers.
- Track whether contract upgrade offers reduce churn.

### 3. Investigate Fiber Optic Customer Experience

Fiber optic service was associated with higher churn risk. This does not prove fiber optic causes churn, but it suggests the segment deserves deeper operational review.

Recommended actions:

- Analyze support tickets, outages, billing complaints, and service expectations for fiber optic customers.
- Compare churn risk by fiber optic tenure and monthly charge level.
- Review whether pricing, reliability, or support experience is driving dissatisfaction.

### 4. Review Electronic Check Payment Friction

Electronic check customers showed elevated churn risk. This may reflect payment friction, customer segment differences, or billing preferences.

Recommended actions:

- Review failed payment rates and billing support interactions.
- Encourage lower-friction automatic payment methods where appropriate.
- Avoid assuming payment method is causal without additional evidence.

### 5. Use Churn Scores as a Prioritization Tool

The model should be used to prioritize review and outreach, not as an automated final decision system.

Recommended actions:

- Create a ranked retention outreach list.
- Combine model risk with business rules such as customer value, tenure, and recent support interactions.
- Track outcomes of outreach to measure whether interventions reduce churn.

## False Positive and False Negative Tradeoff

The selected model favors recall, which is useful for churn detection. It caught many churn customers but also flagged 288 non-churn customers as churn risk.

False negatives are customers who churned but were not flagged. These are the most important missed opportunities.

False positives are customers who were flagged but did not churn. These may still be acceptable if the outreach is low cost and improves customer experience.

Before using this model operationally, the business should estimate:

- Cost of retention outreach.
- Expected value of retaining a customer.
- Outreach team capacity.
- Risk of annoying customers with unnecessary offers.

## Limitations

### Dataset Limitations

- The dataset appears to represent a fictional or sample telecom context.
- It may not reflect current market behavior or a real company's customer base.
- It does not include richer operational signals such as complaints, outages, usage trends, customer satisfaction, or support history.
- It is a static dataset, so it does not evaluate model drift over time.

### Modeling Limitations

- The model is a baseline logistic regression, not an optimized production model.
- The threshold was not tuned.
- Coefficients are associations, not causal explanations.
- Correlated features can make coefficient interpretation less direct.
- The held-out test set was used once for evaluation, but broader validation would be needed before production use.

### Business Limitations

- The project does not estimate customer lifetime value.
- It does not estimate retention campaign cost.
- It does not validate whether recommended interventions actually reduce churn.
- It does not include an operational feedback loop for future retraining.

## Recommended Next Analytical Steps

- Evaluate business impact using expected retention value and outreach cost.
- Add feature importance or coefficient interpretation to the final portfolio README.
- Consider threshold analysis only with a validation set or business-approved cost framework, not by optimizing on the held-out test set.
- Add more realistic data sources if this project is adapted to a real business context.

## Bottom Line

The model is useful as a churn risk prioritization baseline. It can help focus attention on customers most likely to leave, especially early-tenure and month-to-month customers. The next phase should present these findings clearly as portfolio-ready project conclusions while staying honest about limitations.
