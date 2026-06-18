# Model Results Summary

| Model                        | Test Accuracy   | Precision   | Recall   | F1 Score   | ROC-AUC   |   False Positives |   False Negatives |   True Positives |
|:-----------------------------|:----------------|:------------|:---------|:-----------|:----------|------------------:|------------------:|-----------------:|
| Gradient Boosting            | 99.30%          | 94.95%      | 97.92%   | 96.41%     | 99.91%    |                 5 |                 2 |               94 |
| Decision Tree                | 98.90%          | 94.74%      | 93.75%   | 94.24%     | 98.23%    |                 5 |                 6 |               90 |
| Random Forest                | 97.09%          | 78.15%      | 96.88%   | 86.51%     | 99.54%    |                26 |                 3 |               93 |
| Logistic Regression          | 94.38%          | 75.64%      | 61.46%   | 67.82%     | 96.20%    |                19 |                37 |               59 |
| Weighted Logistic Regression | 88.55%          | 45.31%      | 90.62%   | 60.42%     | 96.10%    |               105 |                 9 |               87 |
| Naive Bayes                  | 88.35%          | 41.23%      | 48.96%   | 44.76%     | 91.21%    |                67 |                49 |               47 |
| Dummy Classifier             | 90.36%          | 0.00%       | 0.00%    | 0.00%      | 50.00%    |                 0 |                96 |                0 |
