import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pandas import DataFrame


def bar_plot(
    data: DataFrame, x: str, y: str, xlabel: str, ylabel: str, hue: str = None
):
    ax = sns.barplot(x=x, y=y, data=data, hue=hue)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # putting labels
    for p in ax.patches:
        ax.annotate(
            "{}".format(p.get_width()), (p.get_width(), p.get_y() + 0.3), ha="left"
        )

    plt.show()


def hist_plot(data: DataFrame, x: str, xlabel: str, ylabel: str, hue: str):
    _ = sns.histplot(x=x, data=data, hue=hue)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def ecdf_plot(data: DataFrame, x: str, xlabel: str, ylabel: str, hue: str):
    _ = sns.histplot(
        data=data,
        x=x,
        hue=hue,
        element="step",
        fill=False,
        cumulative=True,
        stat="density",
        common_norm=False,
    )

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def boxplot_plot(
    data: DataFrame,
    x: str,
    y: str,
    xlabel: str,
    ylabel: str,
    hue: str,
    title: str = None,
    horizontal: bool = False,
):

    if horizontal:
        fig_dims = (14, 8)
        fig, ax = plt.subplots(figsize=fig_dims)
    else:
        ax = None

    _ = sns.boxplot(
        x=x,
        y=y,
        data=data,
        hue=hue,
        ax=ax,
    )
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


def plot_confusion_matrix(cf_matrix: np.array, classes: list):
    # text for the plot
    group_names = ["True Neg", "False Pos", "False Neg", "True Pos"]
    group_counts = ["{0:0.0f}".format(value) for value in cf_matrix.flatten()]
    group_percentages = [
        "{0:.2%}".format(value) for value in cf_matrix.flatten() / np.sum(cf_matrix)
    ]
    labels = [
        f"{v1}\n{v2}\n{v3}"
        for v1, v2, v3 in zip(group_names, group_counts, group_percentages)
    ]

    labels = np.asarray(labels).reshape(2, 2)

    # plotting
    ax = sns.heatmap(cf_matrix, annot=labels, fmt="", cmap="Blues")

    ax.set_title("Seaborn Confusion Matrix with labels\n\n")
    ax.set_xlabel("\nPredicted Values")
    ax.set_ylabel("Actual Values ")

    # Ticket labels - List must be in alphabetical order
    # [False, True]
    ax.xaxis.set_ticklabels(classes)
    ax.yaxis.set_ticklabels(classes)

    ## Display the visualization of the Confusion Matrix.
    plt.show()
