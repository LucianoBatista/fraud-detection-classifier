import pickle
import timeit

import pandas as pd

from preprocessing.utils_preprocessing import PreProcessingPipe, Training


def main():
    model_file_name = "models/lrc_baseline.sav"

    start = timeit.default_timer()
    # data
    fraud_df = pd.read_csv("data/fraud_detection_dataset.csv")

    # Pre-processing Pipeline
    pre_processing_pipe = PreProcessingPipe(dataset=fraud_df)
    pre_processing_pipe.drop_columns(
        columns=["isFlaggedFraud", "step", "nameOrig", "nameDest"]
    )
    pre_processing_pipe.filter_type_classes(classes=["PAYMENT", "CASH_IN", "DEBIT"])
    pre_processing_pipe.train_test_splitting(sample_test_size=0.40, to_drop=["isFraud"])
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
    confusion_matrix = training_pipe.get_confusion_matrix()
    metrics = training_pipe.calculate_metrics()

    pickle.dump(training_pipe.lrc, open(model_file_name, "wb"))
    training_pipe.save_confusion_matrix(
        classes=["Not Fraud", "Fraud"], name_to_save=model_file_name.split(".")[0]
    )
    print(confusion_matrix)
    print(metrics)

    stop = timeit.default_timer()
    print("Time: ", stop - start)


if __name__ == "__main__":
    main()
