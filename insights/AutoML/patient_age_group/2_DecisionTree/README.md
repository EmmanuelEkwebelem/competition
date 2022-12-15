# Summary of 2_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: gini
- **max_depth**: 3
- **num_class**: 8
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

6.9 seconds

### Metric details
|           |   adolescent |   adult |   child |   elderly |   mature adult |   senior |   teen |   young adult |   accuracy |    macro avg |   weighted avg |   logloss |
|:----------|-------------:|--------:|--------:|----------:|---------------:|---------:|-------:|--------------:|-----------:|-------------:|---------------:|----------:|
| precision |            0 |       1 |       1 |         1 |              1 |        1 |      0 |      0.423232 |    0.86256 |     0.677904 |       0.804391 |   0.25755 |
| recall    |            0 |       1 |       1 |         1 |              1 |        1 |      0 |      1        |    0.86256 |     0.75     |       0.86256  |   0.25755 |
| f1-score  |            0 |       1 |       1 |         1 |              1 |        1 |      0 |      0.594748 |    0.86256 |     0.699343 |       0.821689 |   0.25755 |
| support   |         1246 |    4891 |    3159 |      1036 |           3171 |     2025 |   1331 |   1891        |    0.86256 | 18750        |   18750        |   0.25755 |


## Confusion matrix
|                         |   Predicted as adolescent |   Predicted as adult |   Predicted as child |   Predicted as elderly |   Predicted as mature adult |   Predicted as senior |   Predicted as teen |   Predicted as young adult |
|:------------------------|--------------------------:|---------------------:|---------------------:|-----------------------:|----------------------------:|----------------------:|--------------------:|---------------------------:|
| Labeled as adolescent   |                         0 |                    0 |                    0 |                      0 |                           0 |                     0 |                   0 |                       1246 |
| Labeled as adult        |                         0 |                 4891 |                    0 |                      0 |                           0 |                     0 |                   0 |                          0 |
| Labeled as child        |                         0 |                    0 |                 3159 |                      0 |                           0 |                     0 |                   0 |                          0 |
| Labeled as elderly      |                         0 |                    0 |                    0 |                   1036 |                           0 |                     0 |                   0 |                          0 |
| Labeled as mature adult |                         0 |                    0 |                    0 |                      0 |                        3171 |                     0 |                   0 |                          0 |
| Labeled as senior       |                         0 |                    0 |                    0 |                      0 |                           0 |                  2025 |                   0 |                          0 |
| Labeled as teen         |                         0 |                    0 |                    0 |                      0 |                           0 |                     0 |                   0 |                       1331 |
| Labeled as young adult  |                         0 |                    0 |                    0 |                      0 |                           0 |                     0 |                   0 |                       1891 |

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

### Dependence adolescent (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_adolescent.png)
### Dependence adult (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_adult.png)
### Dependence child (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_child.png)
### Dependence elderly (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_elderly.png)
### Dependence mature adult (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_mature adult.png)
### Dependence senior (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_senior.png)
### Dependence teen (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_teen.png)
### Dependence young adult (Fold 1)
![SHAP Dependence from fold 1](learner_fold_0_shap_dependence_class_young adult.png)

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
