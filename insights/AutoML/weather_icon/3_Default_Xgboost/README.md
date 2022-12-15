# Summary of 3_Default_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: multi:softprob
- **eta**: 0.075
- **max_depth**: 6
- **min_child_weight**: 1
- **subsample**: 1.0
- **colsample_bytree**: 1.0
- **eval_metric**: mlogloss
- **num_class**: 6
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

7.7 seconds

### Metric details
|           |   clear-day |    cloudy |   partly-cloudy-day |        rain |      snow |      wind |   accuracy |   macro avg |   weighted avg |   logloss |
|:----------|------------:|----------:|--------------------:|------------:|----------:|----------:|-----------:|------------:|---------------:|----------:|
| precision |    0.663158 |  0.439024 |            0.662112 |    0.798103 |  0.695652 |  0.382353 |   0.723823 |    0.606734 |       0.720542 |  0.596477 |
| recall    |    0.558758 |  0.553846 |            0.648418 |    0.839031 |  0.813559 |  0.288889 |   0.723823 |    0.617084 |       0.723823 |  0.596477 |
| f1-score  |    0.606498 |  0.489796 |            0.655194 |    0.818056 |  0.75     |  0.329114 |   0.723823 |    0.60811  |       0.720853 |  0.596477 |
| support   |  451        | 65        |          822        | 1404        | 59        | 45        |   0.723823 | 2846        |    2846        |  0.596477 |


## Confusion matrix
|                              |   Predicted as clear-day |   Predicted as cloudy |   Predicted as partly-cloudy-day |   Predicted as rain |   Predicted as snow |   Predicted as wind |
|:-----------------------------|-------------------------:|----------------------:|---------------------------------:|--------------------:|--------------------:|--------------------:|
| Labeled as clear-day         |                      252 |                    11 |                              112 |                  73 |                   2 |                   1 |
| Labeled as cloudy            |                        3 |                    36 |                               10 |                  14 |                   2 |                   0 |
| Labeled as partly-cloudy-day |                       65 |                    18 |                              533 |                 186 |                  14 |                   6 |
| Labeled as rain              |                       60 |                    17 |                              132 |                1178 |                   3 |                  14 |
| Labeled as snow              |                        0 |                     0 |                                6 |                   5 |                  48 |                   0 |
| Labeled as wind              |                        0 |                     0 |                               12 |                  20 |                   0 |                  13 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Precision Recall Curve

![Precision Recall Curve](precision_recall_curve.png)



## SHAP Importance
![SHAP Importance](shap_importance.png)

## SHAP Dependence plots

### Dependence clear-day (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_clear-day.png)
### Dependence cloudy (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_cloudy.png)
### Dependence partly-cloudy-day (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_partly-cloudy-day.png)
### Dependence rain (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_rain.png)
### Dependence snow (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_snow.png)
### Dependence wind (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_wind.png)

## SHAP Decision plots

### Worst decisions for selected sample 1 (Fold 1)
![SHAP worst decisions from Fold 1](learner_fold_0_sample_0_worst_decisions.png)
### Worst decisions for selected sample 2 (Fold 1)
![SHAP worst decisions from Fold 1](learner_fold_0_sample_1_worst_decisions.png)
### Worst decisions for selected sample 3 (Fold 1)
![SHAP worst decisions from Fold 1](learner_fold_0_sample_2_worst_decisions.png)
### Worst decisions for selected sample 4 (Fold 1)
![SHAP worst decisions from Fold 1](learner_fold_0_sample_3_worst_decisions.png)
### Best decisions for selected sample 1 (Fold 1)
![SHAP best decisions from Fold 1](learner_fold_0_sample_0_best_decisions.png)
### Best decisions for selected sample 2 (Fold 1)
![SHAP best decisions from Fold 1](learner_fold_0_sample_1_best_decisions.png)
### Best decisions for selected sample 3 (Fold 1)
![SHAP best decisions from Fold 1](learner_fold_0_sample_2_best_decisions.png)
### Best decisions for selected sample 4 (Fold 1)
![SHAP best decisions from Fold 1](learner_fold_0_sample_3_best_decisions.png)

[<< Go back](../README.md)
