# Deployment Evidence Checklist

## Local API Evidence

```bash
python flask_app/app.py
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d @flask_app/sample_request.json
```

## Docker Evidence

```bash
docker build -f docker/Dockerfile -t bank-loan-propensity-api:latest .
docker run -p 5000:5000 bank-loan-propensity-api:latest
docker ps
```

## Kubernetes Evidence

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl get pods
kubectl get svc
```

## AWS Evidence

```bash
terraform init
terraform plan
terraform apply
```