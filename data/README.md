# Data Directory

This project expects the original raw banking customer files to be placed in `data/raw/` before running the pipeline.

Expected raw files:

| File | Purpose |
|---|---|
| `Data1.csv` | First customer-level raw data file |
| `Data2.csv` | Second customer-level raw data file joined by `ID` |

Generated processed files:

| File | Created By | Purpose |
|---|---|---|
| `01_merged_customer_data.csv` | `python -m src.data_preprocessing` | One-to-one customer-level merge |
| `02_cleaned_customer_data.csv` | `python -m src.data_preprocessing` | Cleaned customer modeling table |
| `03_train_data.csv` | `python -m src.feature_engineering` | Training split |
| `03_test_data.csv` | `python -m src.feature_engineering` | Test split |

Raw and processed CSV files are intentionally excluded from Git using `.gitignore`.
