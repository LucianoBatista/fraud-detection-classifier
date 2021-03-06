---
title: Metrics
authors:
    - Luciano
---

After the training and prediction steps, all the metrics will be collected and added on this report.

## :fontawesome-solid-space-shuttle: Perfomance Table

Keep tracking of your experiments is a very important task of the Data Scientist, so check the following table to have all the information about the models trained during the challenge of Fraud Detection.

| Model | Precision | Recall | Accuracy | AUC | F1 | Time (s) |
| :-----: | --------- | ------ | -------- | --- | -- | ------------ |
| baseline | 0.964 | 0.082 | 0.997 | 0.541 | **0.153** | 26.77 |
| model-v1 | 0.843 | 0.446 | 0.999 | 0.722 | **0.584** | 99.96 |
| model-v2 | 0.669 | 0.569 | 0.999 | 0.784 | **0.615** | 98.99 |
| model-v3 | 0.027 | *0.877* | 0.958 | 0.918 | **0.052** | 98.94 |
| :fontawesome-regular-laugh-wink: model-v4 | 0.696 | 0.676 | 0.999 | 0.838 | **0.686** | 252.80 |


## :fontawesome-solid-star: Best Model

I choose to pick the model with the best value of **F1 score**. This model could be more balanced between all others trained, and for not overfitting during the training.

This model got right **67.6% of the frauds** that actually is fraud. And, from **all predictions on fraud, 69.6% was right**.

I believe that this result will not dethrone American Express, but now, I can work on improve those models with another techniques of balancing and hyperparameter tuning to increase the F1 score.



