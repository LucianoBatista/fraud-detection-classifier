---
title: Model-v4
authors: 
    - Luciano
---

These was the steps of the *model-v4* using **Random Forest**, I also used feature engineering and numerical and categorical transformations. 

The model is `21_01_22_lr_w_v3.sav`, and can be found on the respective directory.

## Pipeline

```mermaid
graph TD
  A[Transformed Data: second-eda-output.csv] --> B[Type conversion];
  B[Type conversion] --> C[Train Test Split];
  C[Train Test Split] --> D[One Hot Encoder on all categorical variables];
  D[One Hot Encoder] --> E[Fit Random Forest];
  E --> G[Predict];
  G[Predict] --> H[Calculate Metrics];
  classDef tune fill:#f96;
```

## Confusion Matrix

![confusion-matrix](imgs/21_01_22_lr_w_v3.png)


## Feature Importance

![feat-importance](imgs/feat-importance.png)