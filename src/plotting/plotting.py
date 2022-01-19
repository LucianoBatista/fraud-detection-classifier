from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns


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
