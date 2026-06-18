## Bank Loan Propensity Prediction & AWS MLOps Deployment

End-to-end machine learning and deployment-ready MLOps project that predicts high-propensity banking customers for loan campaign targeting. The project combines data cleaning, exploratory analysis, statistical review, feature engineering, classification modelling, model selection, Flask API development, Docker containerization, Kubernetes manifests, Terraform templates, and CI workflow design.

---

## Executive Summary

I developed a finance-focused machine learning project to identify retail banking customers who are most likely to accept a loan offer. The goal is to help a bank improve campaign targeting, reduce unnecessary outreach, and prioritize customers with stronger loan acceptance probability.

The project is designed to reflect the workflow expected in Canadian banking and finance analytics roles: business problem framing, data quality review, exploratory analysis, model development, model evaluation, business interpretation, and deployment readiness.

After comparing multiple classification models and model variants, a tuned Hist Gradient Boosting model was selected as the final champion model because it provided the strongest balance of precision, recall, F1 score, ROC-AUC, and business usability.

---

## Business Problem

Retail banks often run targeted campaigns to promote loan products. Sending offers to every customer can increase marketing costs, reduce campaign efficiency, and create unnecessary customer outreach.

This project answers the question:

> Which customers are most likely to accept a loan offer, and how can the bank prioritize them for targeted campaign outreach?

### Business Objective

Build a machine learning model that predicts whether a customer is likely to accept a loan offer using customer-level banking and demographic features.

### Business Value

- Improve loan campaign targeting
- Reduce unnecessary marketing spend
- Increase return on marketing investment
- Support customer segmentation
- Provide a repeatable scoring pipeline
- Enable API-based model serving for future deployment

---

## Project Highlights

- Built and compared 20+ machine learning model variants for loan propensity prediction
- Applied data cleaning, EDA, statistical testing, feature engineering, and model evaluation
- Handled class imbalance using resampling and model-based approaches
- Tuned candidate models and selected a final production model based on both technical and business metrics
- Achieved **99.93% ROC-AUC** and **96.84% F1 Score** with a **tuned Hist Gradient Boosting model**
- Correctly identified **92 of 96 actual loan customers**, achieving **95.83% Recall**
- Maintained 97.87% Precision, with **only 2 unnecessary marketing targets**
- Deployed the model as a Flask prediction API
- Containerized the application using Docker
- Deployed the service to Amazon EKS using Kubernetes
- Automated infrastructure provisioning with Terraform
- Implemented CI/CD deployment flow using AWS CodePipeline, CodeBuild, and Amazon ECR

---

## Final Production Model

### Tuned Hist Gradient Boosting Classifier

The final model was selected because it provided the best overall balance between identifying likely borrowers and minimizing unnecessary marketing outreach.

| Metric          |  Score |
| --------------- | -----: |
| ROC-AUC         | 99.93% |
| Precision       | 97.87% |
| Recall          | 95.83% |
| F1 Score        | 96.84% |
| Accuracy        | 99.40% |
| False Positives |      2 |
| False Negatives |      4 |

### Business Interpretation

Out of 96 customers who accepted a loan offer in the test dataset, the model correctly identified 92 and missed only 4.

At the same time, only 2 non-borrowers were incorrectly classified as likely borrowers. This means the model can support highly targeted marketing campaigns while keeping unnecessary outreach low.

From a banking business perspective, this model is useful when the goal is to balance campaign conversion opportunity with marketing cost control.

---

## Business Alternative Model

### Random Forest with SMOTE and Undersampling

| Metric          | Result |
| --------------- | -----: |
| Recall          | 98.96% |
| False Negatives |      1 |

**When to use:** This model may be preferred if the business objective is to capture as many potential loan customers as possible, even if that results in more false positives and higher marketing costs.

### Model Selection Decision

| Business Priority                     | Recommended Model                     |
| ------------------------------------- | ------------------------------------- |
| Balanced precision and recall         | Tuned Hist Gradient Boosting          |
| Minimize missed borrowers             | Random Forest + SMOTE + Undersampling |
| Reduce unnecessary campaign targeting | Tuned Hist Gradient Boosting          |
| Maximize marketing reach              | Random Forest + SMOTE + Undersampling |

---

## Key Business Insights

Feature importance analysis showed that the strongest drivers of loan adoption were related to customer spending behaviour, customer value level, internal scoring, and existing banking relationships.

| Rank | Feature             |
| ---: | ------------------- |
|    1 | HighestSpend        |
|    2 | Level               |
|    3 | HiddenScore         |
|    4 | MonthlyAverageSpend |
|    5 | FixedDepositAccount |

Customers were more likely to accept loan offers when they:

- Had higher individual transaction values
- Maintained higher monthly average spending
- Belonged to higher-value customer segments
- Had stronger internal customer scores
- Held fixed deposit accounts with the bank

These insights can help marketing and product teams design more targeted loan campaigns.

---

## Machine Learning Workflow

```text
Raw Customer Data
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Statistical Testing
      ↓
Feature Engineering
      ↓
Class Imbalance Handling
      ↓
Model Training
      ↓
Model Comparison
      ↓
Hyperparameter Tuning
      ↓
Final Model Selection
      ↓
Model Serialization
      ↓
Flask API Deployment
```

---

## AWS MLOps Deployment Workflow

```text
GitHub Repository
      ↓
AWS CodePipeline
      ↓
AWS CodeBuild
      ↓
Docker Image Build
      ↓
Amazon ECR
      ↓
Amazon EKS
      ↓
Kubernetes Deployment
      ↓
Flask Prediction API
      ↓
Customer Propensity Score
```

Infrastructure templates are included in `terraform/`, and Kubernetes deployment manifests are included in `kubernetes/`.

---

## System Architecture

```text
Customer Data
      ↓
Data Validation
      ↓
Feature Engineering
      ↓
Trained ML Model
      ↓
Probability Scoring
      ↓
Flask Prediction API
      ↓
Docker Container
      ↓
Amazon ECR
      ↓
Amazon EKS / Kubernetes
      ↓
Marketing Campaign System
```

---

## Dataset Overview

| Metric            | Value                      |
| ----------------- | -------------------------- |
| Initial Records   | 5,000                      |
| Final Records     | 4,980                      |
| Features          | 14                         |
| Target Variable   | LoanOnCard                 |
| Problem Type      | Binary Classification      |
| Business Use Case | Loan Propensity Prediction |

---

## Models Evaluated

- Baseline and Candidate Models
- Logistic Regression
- Weighted Logistic Regression
- Naive Bayes
- Support Vector Machine
- Decision Tree
- Random Forest
- Hist Gradient Boosting
- AdaBoost

### Experimentation Areas
- Baseline model comparison
- Multicollinearity analysis
- Log transformation of skewed features
- Feature selection
- Class imbalance handling
- SMOTE
- Hybrid resampling
- Hyperparameter tuning
- Precision-recall trade-off analysis
- Business threshold interpretation

---

## Final Model Comparison

| Rank | Model | ROC-AUC | Precision | Recall | F1-Score | False Positives | False Negatives |
|------:|--------|---------:|----------:|-------:|---------:|----------------:|----------------:|
| 1 | Hist Gradient Boosting (Tuned) | 99.93% | 97.87% | 95.83% | 96.84% | 2 | 4 |
| 2 | Random Forest (Baseline) | 99.91% | 98.90% | 93.75% | 96.26% | 1 | 6 |
| 3 | Random Forest + SMOTE + Undersampling | 99.90% | 92.23% | 98.96% | 95.48% | 8 | 1 |

The final production candidate was selected based on its strong overall performance and practical business balance between conversion opportunity and marketing cost control.

---

## Model Validation and Risk Considerations

Because this is a banking analytics use case, the model was evaluated beyond accuracy alone.

Key validation considerations included:

- Precision, recall, F1 score, ROC-AUC, and confusion matrix review
- False positive and false negative business impact
- Class imbalance handling
- Model comparison across multiple algorithms
- Review of feature importance for business interpretability
- Production-readiness through API deployment and containerization

In a real banking environment, this model would require additional validation before production use, including fairness testing, data drift monitoring, model-performance monitoring, approval workflows, and periodic retraining.

---

## Important Risk Note

The model achieved very strong results on the available dataset. In a real banking environment, this would require additional validation before production use, including:

- Out-of-time validation
- Fairness and bias testing
- Data drift monitoring
- Model performance monitoring
- Model approval workflow
- Periodic recalibration or retraining
- Documentation for model risk management

This project is a demonstration and should not be treated as a production banking model without further validation.

---

## Project Screenshots

### Final Model Comparison

![Model Comparison](screenshots/model_comparison.png)

### Feature Importance

![Feature Importance](screenshots/feature_importance.png)

### Flask Prediction API

![Flask API](screenshots/flask_api.png)

### Docker Container

![Docker](screenshots/docker_container.png)

### Kubernetes Deployment

![Kubernetes](screenshots/kubernetes_pods.png)

### AWS EKS Deployment

![EKS](screenshots/eks_deployment.png)

### CI/CD Pipeline

![CodePipeline](screenshots/codepipeline.png)

---

## Repository Structure

```text
bank-loan-propensity-mlops/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda_statistical_analysis.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training_evaluation.ipynb
│   └── 05_model_selection.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── predict.py
│
├── flask_app/
│   ├── app.py
│   ├── model/
│   └── requirements.txt
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
├── screenshots/
│   ├── model_comparison.png
│   ├── feature_importance.png
│   ├── flask_api.png
│   ├── docker_container.png
│   ├── kubernetes_pods.png
│   ├── eks_deployment.png
│   └── codepipeline.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/bank-loan-propensity-mlops.git
cd bank-loan-propensity-mlops
```

---

### 2. Create and activate environment

```bash
python -m venv .venv
```

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4. Add the raw data locally

Place the raw datasets at:

```text
data/raw/Data1.csv
data/raw/Data2.csv
```

Raw data is intentionally excluded from GitHub to keep the repository clean and avoid sharing source data publicly.

---

### 5. Run the full source-code pipeline

Run these commands from the project root:

```bash
python -m src.data_preprocessing
python -m src.feature_engineering
python -m src.train_model
python -m src.predict
```

The pipeline will:

```text
Load raw customer datasets
        ↓
Merge and validate customer records
        ↓
Clean the target and modeling features
        ↓
Create train-test datasets
        ↓
Train and evaluate the final model
        ↓
Save model artifacts
        ↓
Run a sample prediction
```

---

### 6. Run notebooks in order

Open and run the notebooks from `01` to `05`:

```text
notebooks/01_data_understanding.ipynb
notebooks/02_eda_statistical_analysis.ipynb
notebooks/03_feature_engineering.ipynb
notebooks/04_model_training_evaluation.ipynb
notebooks/05_model_selection.ipynb
```

The notebooks explain both the technical implementation and the business reasoning behind each modeling decision.

---

### 7. Run the Flask API locally

After training the model, start the API:

```bash
python flask_app/app.py
```

The API will run at:

```text
http://localhost:5000
```

Send a sample prediction request:

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d @flask_app/sample_request.json
```

#### Example Request

```json
{
  "Age": 42,
  "Experience": 16,
  "Income": 120,
  "Family": 3,
  "CCAvg": 4.2,
  "Education": 2,
  "Mortgage": 0,
  "SecuritiesAccount": 0,
  "CDAccount": 1,
  "Online": 1,
  "CreditCard": 1
}
```
#### Example response:

```json
{
  "success": true,
  "prediction": 1,
  "propensity_label": "High Propensity",
  "loan_acceptance_probability": 0.94
}
```

---

### 8. Run with Docker

Build the Docker image:

```bash
docker build -f docker/Dockerfile -t bank-loan-propensity-api:latest .
```

Run the container:

```bash
docker run -p 5000:5000 bank-loan-propensity-api:latest
```

---

### 9. Deploy with Kubernetes

Update the image name in `kubernetes/deployment.yaml`, then run:

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl get pods
kubectl get svc
```

---

### 10. Provision AWS infrastructure with Terraform

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

> Note: Terraform may create billable AWS resources. Review the configuration and destroy unused resources after testing.

```bash
terraform destroy
```

---

## Business Use Case

The model can be used by a retail bank’s marketing analytics team to score customers before launching a loan campaign.

A typical workflow would be:

1. Score customers using the prediction API
2. Rank customers by loan acceptance probability
3. Select high-propensity customers for outreach
4. Monitor campaign conversion rates
5. Retrain or recalibrate the model as customer behaviour changes

---

## Technology Stack

### Data Science and Machine Learning

- Python
- Pandas
- NumPy
- Scikit-Learn
- Imbalanced-Learn
- SciPy
- Matplotlib
- Seaborn
- 
### Application Development

- Flask
- REST API
- Model serialization
- API testing
- 
### Cloud and MLOps

- AWS
- Amazon EKS
- Amazon ECR
- AWS CodePipeline
- AWS CodeBuild
- Docker
- Kubernetes
- Terraform
- CI/CD

---

## Skills Demonstrated

### Data Science

- Business problem framing
- Data cleaning
- Exploratory data analysis
- Statistical analysis
- Feature engineering
- Classification modeling
- Class imbalance handling
- Hyperparameter tuning
- Model evaluation
- Feature importance analysis
- Business metric interpretation

### Banking and Analytics

- Loan propensity modeling
- Customer targeting
- Campaign optimization
- Marketing cost reduction
- Precision-recall trade-off analysis
- Customer segmentation support
- Banking product analytics

### MLOps and Deployment

- Flask API development
- Docker containerization
- Kubernetes deployment
- Amazon EKS deployment
- Amazon ECR image registry
- Terraform infrastructure provisioning
- CI/CD pipeline design
- Cloud-native ML deployment

---

## Target Roles This Project Supports

This project was structured to reflect skills commonly requested in Canadian banking and finance analytics roles:

| Target role | Project evidence |
|---|---|
| Python analytics | End-to-end notebooks and reusable `src/` pipeline |
| Statistical analysis | EDA, distribution review, categorical analysis, and model interpretation |
| Credit / banking context | Customer-level loan propensity and campaign targeting use case |
| Machine learning | Multiple classification models, tuning, and model selection |
| Model evaluation | Precision, recall, F1, ROC-AUC, confusion matrix, false-positive/false-negative analysis |
| MLOps readiness | Flask API, Dockerfile, Kubernetes manifests, Terraform templates, CI workflow |
| Business communication | README explains model results in banking and campaign terms |

---

## Future Enhancements

- Add automated model retraining pipeline
- Add model monitoring and drift detection
- Add data quality validation before scoring
- Add fairness and bias testing
- Add model registry and experiment tracking
- Add Prometheus and Grafana monitoring
- Add GitOps deployment using ArgoCD
- Add A/B testing for marketing campaign optimization
- Add batch scoring pipeline for large customer files
- Add dashboard for business users

---

## Conclusion

This project demonstrates how machine learning can be applied to a real banking business problem and deployed through a cloud-native MLOps workflow.

The final tuned Hist Gradient Boosting model achieved 99.93% ROC-AUC and 96.84% F1 Score while maintaining strong precision and recall. The solution also shows how a model can move beyond notebook experimentation into an API-based deployment using Docker, Kubernetes, Terraform, Amazon EKS, and AWS CI/CD services.

This project is designed to demonstrate practical skills for finance data analyst, data scientist, machine learning analyst, banking analytics, and MLOps-focused roles in the Canadian financial services industry.
