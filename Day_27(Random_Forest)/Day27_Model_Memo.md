Day27 Model Memo

1. Objective

The objective was to predict Titanic passenger survival using 1,000
passenger records. The model used six features: pclass, sex_male,
age, sibsp, parch, and fare. Missing age values were filled
using the median within pclass/sex groups, and missing fare values
were filled with the overall median.

2. Model choice

Random Forest is a suitable baseline because it combines many decision
trees, reducing the instability of a single tree. It can capture
nonlinear relationships and interactions without requiring feature
scaling. Bootstrap sampling and OOB evaluation also make it useful for
assessing model performance while training.

3. Evaluation

The selected model uses 100 trees with max_features="sqrt". Its
OOB score is 0.7175, test accuracy is 0.6800, and test ROC-AUC
is 0.7680. The OOB score and test accuracy differ by about 0.038, so
OOB performance gives useful but not strong confidence about held-out
performance. In a 25-bootstrap stability experiment, the 200-tree Random
Forest had mean ROC-AUC 0.7664 with standard deviation 0.0143,
indicating relatively stable performance across training-data changes.

4. Key findings

sex_male is an important predictor. Permutation importance
ranked it first with a score of 0.2042, and its PDP showed a
negative relationship with predicted survival probability.

fare shows a generally positive model relationship. Its
permutation importance was 0.0157, and the PDP showed that
predicted survival probability generally increases as fare
increases, with some fluctuations. These are model relationships,
not causal effects.

5. Risks and limitations

The dataset is relatively small, so results may vary across
splits.

Correlation is not causation; PDPs describe model behavior
rather than real-world causal effects.

Impurity importance can be biased: random_noise ranked 4th
with impurity importance (0.1954) but only 5th with permutation
importance (0.0015).

Missing values were imputed, which adds uncertainty.

The OOB score and held-out test accuracy are not identical, so test
performance has uncertainty.

Historical Titanic data may contain patterns that should not be
generalized to modern populations, and features such as sex raise
fairness considerations.

6. Recommendation

Use this Random Forest as a baseline, but next compare it with
Logistic Regression and Gradient Boosting using cross-validation.
This will show whether the Random Forest's nonlinear modeling provides a
meaningful and reliable improvement over simpler and alternative models.

