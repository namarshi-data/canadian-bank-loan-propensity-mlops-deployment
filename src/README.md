# Source Code Package

Reusable production-style code extracted from the notebooks.

| File | Purpose |
|---|---|
| `config.py` | Central project paths, feature lists, and constants |
| `data_preprocessing.py` | Load, merge, clean, and validate raw datasets |
| `feature_engineering.py` | Prepare features and create train-test datasets |
| `evaluate_model.py` | Evaluate models and calculate FP/FN business metrics |
| `train_model.py` | Train, tune, evaluate, and save model artifacts |
| `predict.py` | Load saved model and generate customer predictions |

Execution order:

```bash
python -m src.data_preprocessing
python -m src.feature_engineering
python -m src.train_model
python -m src.predict
```
