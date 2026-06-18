# Canadian Bank Loan Propensity Prediction & MLOps Deployment

I built this project to predict high-propensity banking customers for personal loan marketing and to package the solution in a deployment-ready MLOps structure.

The project is designed as a finance and data science portfolio project for Canadian banking, analytics, and machine learning roles. It demonstrates data cleaning, exploratory analysis, statistical review, feature engineering, classification modelling, business-focused model evaluation, Flask API development, Docker packaging, Kubernetes manifests, Terraform templates, unit testing, and GitHub Actions CI validation.

> **Deployment status:** This repository is deployment-ready. It includes Docker, Kubernetes, Terraform, and CI templates. It does not claim a live AWS deployment unless real deployment evidence is added later.

---

## Business Problem

Retail banks need to prioritize customers who are most likely to respond to loan campaigns. Broad campaigns can increase marketing costs, reduce customer experience, and waste sales capacity by targeting customers with low likelihood of conversion.

This project answers:

* Which customers are most likely to accept a personal loan offer?
* Which customer attributes are most associated with loan propensity?
* Which model provides the best balance between customer capture and campaign efficiency?
* How can the model be packaged for repeatable API-based scoring?

---

## Executive Summary

The final champion model is a Gradient Boosting classifier with a tuned classification threshold. It was selected because it provided the strongest balance between identifying likely loan customers and controlling unnecessary campaign outreach.

| Metric          | Result |
| --------------- | -----: |
| ROC-AUC         | 99.91% |
| Precision       | 94.95% |
| Recall          | 97.92% |
| F1 Score        | 96.41% |
| False Positives |      5 |
| False Negatives |      2 |

### Business Interpretation

In the holdout set, the model correctly identified **94 of 96 actual loan customers** and missed only **2**. It incorrectly targeted **5 non-loan customers**.

From a banking campaign perspective, this model supports targeted outreach by helping marketing teams prioritize customers with stronger loan acceptance probability while keeping unnecessary contact volume low.

---

## Business Value

This project demonstrates how a retail bank could use predictive analytics to support personal loan campaign planning.

Potential business benefits include:

* Better campaign targeting
* Reduced unnecessary outreach
* Improved sales team prioritization
* Higher return on marketing investment
* Customer-level propensity scoring
* Repeatable scoring through an API-ready pipeline

---

## Project Workflow

```text
Raw customer data
        ↓
Data cleaning and preprocessing
        ↓
EDA and statistical analysis
        ↓
Feature engineering
        ↓
Train-test split
        ↓
Model training and evaluation
        ↓
Threshold tuning
        ↓
Champion model selection
        ↓
Model governance review
        ↓
Flask prediction API
        ↓
Docker / Kubernetes / Terraform templates
        ↓
CI validation with GitHub Actions
```

---

## Repository Structure

```text
canadian-bank-loan-propensity-mlops-deployment/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│   ├── raw/
│   │   └── .gitkeep
│   ├── processed/
│   │   └── .gitkeep
│   └── README.md
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning_preprocessing.ipynb
│   ├── 03_eda_statistical_analysis.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training_evaluation.ipynb
│   └── 06_model_selection_governance.ipynb
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── evaluate_model.py
│   ├── train_model.py
│   ├── predict.py
│   └── utils.py
│
├── flask_app/
│   ├── app.py
│   ├── sample_request.json
│   ├── test_api.py
│   ├── requirements.txt
│   └── model/
│       └── .gitkeep
│
├── scripts/
│   └── run_pipeline.py
│
├── tests/
│   ├── test_preprocessing.py
│   └── test_prediction_contract.py
│
├── docker/
│   └── Dockerfile
│
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── docs/
│   ├── deployment_evidence_checklist.md
│   ├── model_card.md
│   ├── model_results_summary.md
│   └── recruiter_review_notes.md
│
├── screenshots/
│   ├── architecture.png
│   ├── project_workflow.png
│   ├── model_comparison.png
│   └── feature_importance.png
│
├── requirements.txt
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## Notebook Guide

| Notebook                               | Purpose                                                                                                            |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `01_data_understanding.ipynb`          | Understand the raw files, schema, customer-level records, target variable, and business use case                   |
| `02_data_cleaning_preprocessing.ipynb` | Merge raw files, validate data quality, handle missing targets, correct inconsistent values, and save cleaned data |
| `03_eda_statistical_analysis.ipynb`    | Analyze target imbalance, feature distributions, customer behaviour, and loan propensity patterns                  |
| `04_feature_engineering.ipynb`         | Create modelling-ready features, avoid identifier leakage, and generate train-test datasets                        |
| `05_model_training_evaluation.ipynb`   | Train candidate models and compare precision, recall, F1, ROC-AUC, false positives, and false negatives            |
| `06_model_selection_governance.ipynb`  | Select the champion model, tune the classification threshold, and document governance considerations               |

---

## Source Code Pipeline

The notebooks explain the analytical reasoning. The `src/` package contains reusable production-style Python code so the project can be run as a repeatable pipeline.

Run the full pipeline:

```bash
python scripts/run_pipeline.py
```

Or run each step separately:

```bash
python -m src.data_preprocessing
python -m src.feature_engineering
python -m src.train_model
python -m src.predict
```

The source pipeline performs:

```text
raw data loading
        ↓
customer-level merge
        ↓
data cleaning and validation
        ↓
feature preparation
        ↓
train-test split
        ↓
model training
        ↓
model evaluation
        ↓
model artifact export
```

---

## Dataset Overview

| Item                          |                               Value |
| ----------------------------- | ----------------------------------: |
| Initial records               |                               5,000 |
| Final cleaned records         |                               4,980 |
| Holdout actual loan customers |                                  96 |
| Target variable               |                        `LoanOnCard` |
| Problem type                  |               Binary classification |
| Business use case             | Personal loan propensity prediction |

Raw data is intentionally excluded from GitHub. Place the raw files locally under `data/raw/`.

---

## Final Champion Model

The champion model is a Gradient Boosting classifier with a tuned classification threshold of **0.49**.

| Metric           | Result |
| ---------------- | -----: |
| ROC-AUC          | 99.91% |
| Precision        | 94.95% |
| Recall           | 97.92% |
| F1 Score         | 96.41% |
| False Positives  |      5 |
| False Negatives  |      2 |
| True Positives   |     94 |
| Actual Positives |     96 |

### Why This Model Was Selected

The selected model provides a strong business balance:

* High recall means most actual loan customers are captured.
* Strong precision means the campaign is not overloaded with too many low-propensity customers.
* Low false negatives reduce missed revenue opportunity.
* Low false positives help control unnecessary campaign cost.

---

## Business Interpretation of Errors

| Error Type     | Meaning in This Project                                             | Business Impact               |
| -------------- | ------------------------------------------------------------------- | ----------------------------- |
| False Positive | Customer predicted as high-propensity but did not accept the loan   | Extra campaign outreach cost  |
| False Negative | Customer predicted as low-propensity but actually accepted the loan | Missed conversion opportunity |

The champion model produced **5 false positives** and **2 false negatives** on the holdout set. For a marketing use case, this is a strong trade-off because missing likely customers is usually more costly than contacting a small number of additional customers.

---

## Feature Importance

The strongest model drivers were related to customer value, transaction behaviour, internal scoring, and existing banking relationships.

| Rank | Feature             |
| ---: | ------------------- |
|    1 | HighestSpend        |
|    2 | Level               |
|    3 | HiddenScore         |
|    4 | MonthlyAverageSpend |
|    5 | FixedDepositAccount |

Customers were more likely to accept loan offers when they had higher transaction values, stronger customer scores, higher banking relationship levels, higher spending behaviour, and existing fixed deposit relationships.

![Feature Importance](screenshots/feature_importance.png)

---

## Model Comparison

The model development process compared multiple baseline and candidate models, including:

* Dummy Classifier
* Logistic Regression
* Weighted Logistic Regression
* Naive Bayes
* Support Vector Machine
* Decision Tree
* Random Forest
* Gradient Boosting
* Resampling-based experiments

The final champion was selected using both technical metrics and business interpretation.

![Model Comparison](screenshots/model_comparison.png)

---

## Model Validation and Governance Notes

Because this is a banking analytics use case, the model was evaluated beyond accuracy alone.

Validation considerations included:

* Precision, recall, F1, and ROC-AUC
* Confusion matrix review
* False positive and false negative business impact
* Class imbalance awareness
* Threshold tuning
* Feature importance interpretation
* Reproducible train-test workflow
* API prediction contract validation

### Important Model Risk Note

This is a portfolio project. It demonstrates professional project structure and deployment readiness, but it should not be used as-is for real customer decisioning.

Before real banking production use, the model would require:

* Fairness and bias testing
* Privacy and consent review
* Out-of-time validation
* Model drift monitoring
* Data quality monitoring
* Approval from model risk and governance stakeholders
* Periodic recalibration or retraining
* Business owner sign-off

---

## Screenshots

### Project Workflow

![Project Workflow](screenshots/project_workflow.png)

### Architecture

![Architecture](screenshots/architecture.png)

### Model Comparison

![Model Comparison](screenshots/model_comparison.png)

### Feature Importance

![Feature Importance](screenshots/feature_importance.png)

> Deployment screenshots should be added only after real execution. Do not include fake AWS, Kubernetes, Docker, or CI/CD screenshots.

---

## How to Run Locally

### 1. Create and activate environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Add raw data locally

Place the raw files here:

```text
data/raw/Data1.csv
data/raw/Data2.csv
```

Raw data is intentionally excluded from GitHub.

### 4. Run the full pipeline

```bash
python scripts/run_pipeline.py
```

This performs:

```text
data cleaning and preprocessing
feature engineering
train-test split
model training
model evaluation
artifact export
```

### 5. Run notebooks

Open and run the notebooks from `01` to `06` in order.

---

## Run the Flask API

Train the model first:

```bash
python scripts/run_pipeline.py
```

Start the API:

```bash
python flask_app/app.py
```

Send a prediction request:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d @flask_app/sample_request.json
```

Example response:

```json
{
  "success": true,
  "result": {
    "prediction": 1,
    "loan_acceptance_probability": 0.94,
    "propensity_label": "High Propensity",
    "classification_threshold": 0.49
  }
}
```

---

## Docker

Build and run the API container locally:

```bash
docker build -f docker/Dockerfile -t bank-loan-propensity-api:latest .
docker run -p 5000:5000 bank-loan-propensity-api:latest
```

---

## Kubernetes

Update the image name in `kubernetes/deployment.yaml`, then run:

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl get pods
kubectl get svc
```

These manifests are included as deployment templates. Add Kubernetes evidence only after running the service in a real cluster.

---

## Terraform

The Terraform folder includes an Amazon ECR repository template for container image publishing.

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

AWS resources may create costs. Destroy resources after testing:

```bash
terraform destroy
```

---

## CI Validation

The GitHub Actions workflow validates the project by:

* Installing dependencies
* Compiling Python files
* Running unit tests
* Building the Docker image

Workflow file:

```text
.github/workflows/ci.yml
```

---

## Technology Stack

### Data Science and Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* Imbalanced-Learn
* SciPy
* Matplotlib
* Seaborn

### Application and API Development

* Flask
* REST API
* Joblib model serialization
* API request/response contract testing

### Engineering and MLOps Readiness

* Modular Python source code
* Single pipeline runner
* Unit tests
* Docker
* Kubernetes manifests
* Terraform templates
* GitHub Actions CI
* Clean artifact and data management

---

## Skills Demonstrated

### Data Science

* Data cleaning and preprocessing
* Exploratory data analysis
* Statistical review
* Feature engineering
* Classification modelling
* Class imbalance awareness
* Threshold tuning
* Precision, recall, F1, and ROC-AUC evaluation
* Confusion matrix interpretation
* Feature importance analysis
* Champion model selection

### Banking and Business Analytics

* Personal loan propensity modelling
* Customer targeting
* Marketing campaign optimization
* Sales prioritization
* False positive and false negative cost interpretation
* Business-focused model evaluation
* Model governance awareness

### Engineering and MLOps

* Reusable Python modules
* Repeatable pipeline execution
* Flask API serving
* Docker container template
* Kubernetes deployment manifests
* Terraform infrastructure template
* GitHub Actions CI workflow
* Unit testing and prediction contract validation

---

## Target Roles This Project Supports

| Target Role                   | Project Evidence                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------- |
| Data Analyst                  | Data cleaning, EDA, business insights, visualizations, reporting-style interpretation |
| Finance Data Analyst          | Banking use case, customer targeting, campaign metric interpretation                  |
| Data Scientist                | Classification modelling, model comparison, threshold tuning, feature importance      |
| Machine Learning Analyst      | Reusable ML pipeline, model evaluation, prediction API, testing                       |
| Banking Analytics Analyst     | Loan propensity modelling, customer segmentation, campaign optimization               |
| MLOps / ML Deployment Analyst | Flask API, Docker, Kubernetes templates, Terraform template, CI workflow              |

---

## Future Enhancements

* Add SQL-based data extraction or analytics layer
* Add Power BI or Tableau dashboard for campaign monitoring
* Add MLflow experiment tracking
* Add model registry workflow
* Add automated drift monitoring
* Add fairness and bias testing
* Add batch scoring for customer campaign files
* Add scheduled retraining pipeline
* Add real AWS ECR/EKS deployment evidence
* Add A/B testing framework for loan campaign strategy

---

## Important Notes

This project is a portfolio demonstration. It shows a professional end-to-end machine learning workflow and deployment-ready structure, but it does not represent an approved production banking model.

The repository intentionally excludes raw data, processed datasets, model artifacts, cloud credentials, Terraform state files, and generated outputs from version control.

---

## Conclusion

This project demonstrates how machine learning can support a practical banking business problem: identifying customers who are most likely to accept a personal loan offer.

The final Gradient Boosting champion model achieved **99.91% ROC-AUC**, **94.95% Precision**, **97.92% Recall**, and **96.41% F1 Score** on the holdout set. More importantly, the project connects model performance to campaign business decisions by explaining false positives, false negatives, recall, precision, and threshold selection.

The project is structured to show both analytical and engineering readiness through clean notebooks, reusable source code, a single pipeline script, a Flask prediction API, unit tests, Docker packaging, Kubernetes manifests, Terraform templates, and GitHub Actions CI validation.

It is designed as a professional portfolio project for Canadian banking analytics, finance data analyst, data scientist, machine learning analyst, and MLOps-oriented roles.
