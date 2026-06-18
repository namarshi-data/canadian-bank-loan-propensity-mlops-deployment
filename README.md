## Bank Loan Propensity Prediction & AWS MLOps Deployment

Finance-focused machine learning and MLOps project that predicts high-propensity loan customers and deploys a scalable prediction API on AWS using Flask, Docker, Kubernetes, Terraform, Amazon EKS, Amazon ECR, and AWS CI/CD services.

---

## Executive Summary

I built an end-to-end machine learning and MLOps solution to identify banking customers who are most likely to accept a loan offer. The project supports targeted marketing by helping a retail bank prioritize high-propensity customers, reduce unnecessary campaign spend, and improve return on marketing investment.

The project covers the full machine learning lifecycle:

- Business problem framing
- Data cleaning and exploratory analysis
- Statistical testing and feature engineering
- Model training and comparison
- Class imbalance handling
- Hyperparameter tuning
- Final model selection
- Flask API development
- Docker containerization
- Kubernetes deployment on Amazon EKS
- Infrastructure provisioning using Terraform
- CI/CD automation using AWS CodePipeline and CodeBuild

After evaluating more than 20 model variations, a tuned Hist Gradient Boosting model was selected as the final production candidate because it delivered the strongest balance of precision, recall, F1 score, and business usability.

---

## Business Problem

Retail banks often run loan marketing campaigns across a broad customer base, which can lead to low conversion rates, unnecessary marketing costs, and poor customer targeting.

The business objective of this project is to predict which customers are most likely to accept a loan offer so that marketing teams can focus outreach on the highest-propensity customers.

This type of solution can help financial institutions:

- Improve campaign targeting
- Increase loan adoption rates
- Reduce customer acquisition costs
- Improve marketing efficiency
- Support data-driven customer segmentation
- Enable scalable customer scoring through an API-based deployment

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

Infrastructure provisioning is automated using Terraform, while deployment is managed through AWS CodePipeline and CodeBuild.

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

## API Usage Example

The deployed Flask API accepts customer-level input features and returns a loan propensity prediction.

### Example Request

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

### Example Response

```json
{
  "prediction": 1,
  "propensity_label": "High Propensity",
  "loan_acceptance_probability": 0.94
}
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
