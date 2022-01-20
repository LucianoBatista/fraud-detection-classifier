---
title: Model-v1
authors:
    - Luciano
---

These was the steps of the *model-v1* using **Logistic Regression**, I also used feature engineering and numerical and categorical transformations. The data was not balanced by any technique and the model was not tunned as well. 

- **File name:** `19_01_22_lr_v1.sav`

## Pipeline

```mermaid
graph TD
  A[Transformed Data: second-eda-output.csv] --> B[Type conversion];
  B[Type conversion] --> C[Train Test Split];
  C[Train Test Split] --> D[One Hot Encoder on all categorical variables];
  D[One Hot Encoder] --> E[Fit Logistic Regression];
  E[Fit Logistic Regression] --> F[Predict];
  F[Predict] --> G[Calculate Metrics];
```
