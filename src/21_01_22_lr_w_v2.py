import pickle
import timeit

import pandas as pd

from preprocessing.utils_preprocessing import PreProcessingPipe, Training


def main():
    model_file_name = "models/21_01_22_lr_w_v2.sav"

    start = timeit.default_timer()

    # data
    fraud_df = pd.read_csv("data/second-eda-output.csv")
    fraud_df["day_of_month"] = fraud_df["day_of_month"].astype(str)

    # Pre-processing Pipeline
    pre_processing_pipe = PreProcessingPipe(dataset=fraud_df)
    pre_processing_pipe.train_test_splitting(
        sample_test_size=0.40, to_drop=["is_fraud"]
    )
    pre_processing_pipe.one_hot_encoder(["day_of_month", "type"])

    # Training
    training_pipe = Training(
        X_train=pre_processing_pipe.X_train,
        X_test=pre_processing_pipe.X_test,
        y_train=pre_processing_pipe.y_train,
        y_test=pre_processing_pipe.y_test,
    )
    training_pipe.fit_logistic_regression(class_weight="balanced")
    training_pipe.predict_logistic_regression()
    metrics = training_pipe.calculate_metrics()

    pickle.dump(training_pipe.lrc, open(model_file_name, "wb"))

    print(training_pipe.get_confusion_matrix())

    training_pipe.save_confusion_matrix(
        classes=["Fraud", "Not Fraud"], name_to_save=model_file_name.split(".")[0]
    )
    print(metrics)

    stop = timeit.default_timer()
    print("Time: ", stop - start)


if __name__ == "__main__":
    main()
