import pickle

import pandas as pd
from src.utils_preprocessing import PreProcessingPipe, Training

model_file_name = "models/19_01_22_lr_v1.sav"

# data
fraud_df = pd.read_csv("data/second-eda-output.csv")
fraud_df["day_of_month"] = fraud_df["day_of_month"].astype(str)
# Pre-processing Pipeline

pre_processing_pipe = PreProcessingPipe(dataset=fraud_df)
pre_processing_pipe.train_test_splitting(sample_test_size=0.40, to_drop=["is_fraud"])
pre_processing_pipe.one_hot_encoder(["day_of_month", "type"])

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
