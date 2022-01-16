from random import sample
from threading import local
import pandas as pd
from pandas import DataFrame
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


class PreProcessingPipe:
    def __init__(self, dataset: DataFrame) -> None:
        self.dataset = dataset
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def validate_columns(self) -> bool:
        columns = self.dataset.columns
        if list(columns) != [
            "step",
            "type",
            "amount",
            "nameOrig",
            "oldbalanceOrg",
            "newbalanceOrig",
            "nameDest",
            "oldbalanceDest",
            "newbalanceDest",
            "isFraud",
            "isFlaggedFraud",
        ]:
            return False
        else:
            return True

    def drop_columns(self, columns: list) -> None:
        self.dataset.drop(columns, axis=1, inplace=True)

    def filter_type_classes(self, classes: list):
        self.dataset = self.dataset[~self.dataset["type"].isin(classes)]

    def train_test_splitting(self, sample_test_size: float):
        X_dataset = self.dataset.drop(["isFraud"], axis=1)
        y_target = self.dataset[["isFraud"]]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X_dataset,
            y_target,
            test_size=sample_test_size,
            random_state=10,
            stratify=y_target,
        )

    def label_encoding(self):
        le = preprocessing.LabelEncoder()
        le.fit(self.X_train["type"])

        # looking at the classes
        print(list(le.classes_))

        self.X_train["type"] = le.transform(self.X_train["type"])
        self.X_test["type"] = le.transform(self.X_test["type"])

    def scaling(self):
        scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))

        scaler.fit(self.X_train)
        X_train_np = scaler.transform(self.X_train)
        x_test_np = scaler.transform(self.X_test)

        self.X_train = pd.DataFrame(X_train_np, columns=self.X_train.columns)
        self.X_test = pd.DataFrame(x_test_np, columns=self.X_test.columns)
