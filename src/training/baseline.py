import pickle

import pandas as pd
from src.preprocessing.utils_preprocessing import PreProcessingPipe, Training

model_file_name = "models/lrc_baseline.sav"

# data
fraud_df = pd.read_csv("data/fraud_detection_dataset.csv")

# Pre-processing Pipeline
pre_processing_pipe = PreProcessingPipe(dataset=fraud_df)
pre_processing_pipe.drop_columns(
    columns=["isFlaggedFraud", "step", "nameOrig", "nameDest"]
)
pre_processing_pipe.filter_type_classes(classes=["PAYMENT", "CASH_IN", "DEBIT"])
pre_processing_pipe.train_test_splitting(sample_test_size=0.40)
pre_processing_pipe.label_encoding()
pre_processing_pipe.scaling()

# Training
training_pipe = Training(
    X_train=pre_processing_pipe.X_train,
    X_test=pre_processing_pipe.X_test,
    y_train=pre_processing_pipe.y_train,
    y_test=pre_processing_pipe.y_test,
)
training_pipe.fit_logistic_regression()
training_pipe.predict_logistic_regression()
metrics = training_pipe.calculate_metrics()

pickle.dump(training_pipe.lrc, open(model_file_name, "wb"))
