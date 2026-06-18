# Data Folder

Raw and processed datasets are not committed to GitHub.

Place the source CSV files here before running the pipeline:

```text
data/raw/Data1.csv
data/raw/Data2.csv
```

The pipeline will generate:

```text
data/processed/01_merged_customer_data.csv
data/processed/02_cleaned_customer_data.csv
data/processed/03_train_data.csv
data/processed/03_test_data.csv
```

This keeps the repository clean while still making the project reproducible.
