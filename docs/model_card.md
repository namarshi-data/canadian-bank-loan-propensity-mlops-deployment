# Model Card: Bank Loan Propensity Model

## Intended Use

This model estimates the probability that an existing banking customer will accept a personal loan offer. The output is intended for marketing prioritization and campaign targeting, not for credit approval or adverse-action decisioning.

## Business Context

Retail banks can reduce campaign cost and improve customer experience by targeting customers who are more likely to be interested in a loan product. The model supports a ranked lead list and a binary high/low propensity label.

## Target Variable

`LoanOnCard`

- `1`: customer accepted or is associated with a loan offer
- `0`: customer did not accept or is not associated with a loan offer

## Model Inputs

The model uses customer demographics, tenure, spending behaviour, mortgage exposure, product holdings, and digital engagement indicators.

## Final Model

Gradient Boosting classifier with threshold tuning.

## Why This Model

The champion model was selected because it provided the best balance of precision, recall, F1 score, and ROC-AUC while still producing interpretable feature-importance diagnostics.

## Limitations

- The dataset is relatively small.
- The features are anonymized and simplified.
- Real production deployment would require drift monitoring, fairness review, model-risk review, privacy review, and approval from governance stakeholders.
- Threshold selection should be finalized on a validation set before final test-set review in a production model-development process.

## Governance Notes

This model is positioned as a portfolio demonstration of supervised learning, business-oriented evaluation, API packaging, and deployment readiness. It should not be used as-is for real customer decisioning.
