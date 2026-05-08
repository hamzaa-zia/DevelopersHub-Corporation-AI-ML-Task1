from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter


OUTPUT_DIR = Path(__file__).resolve().parent
DATA_PATH = OUTPUT_DIR / "superbowl_commercials.csv"


def compact_number(value: float, _: int) -> str:
    """Format large axis values as readable counts such as 250K or 1.5M."""
    if pd.isna(value):
        return ""
    if abs(value) >= 1_000_000:
        return f"{value / 1_000_000:g}M"
    if abs(value) >= 1_000:
        return f"{value / 1_000:g}K"
    return f"{value:g}"


def make_plotting_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Create readable plotting columns without changing the original dataset."""
    return pd.DataFrame(
        {
            "Year": df["Year"],
            "Length (seconds)": df["Length"],
            "Estimated Cost (million USD)": df["Estimated Cost"],
            "YouTube Views (millions)": df["Youtube Views"] / 1_000_000,
            "YouTube Likes (thousands)": df["Youtube Likes"] / 1_000,
            "TV Viewers (millions)": df["TV Viewers"],
        }
    )


def print_dataset_overview(df: pd.DataFrame) -> None:
    """Print the required basic dataset inspection output."""
    print("\nDATASET SHAPE")
    print(df.shape)

    print("\nCOLUMN NAMES")
    print(df.columns.tolist())

    print("\nFIRST FIVE ROWS")
    print(df.head())

    print("\nDATAFRAME INFO")
    df.info()

    print("\nSUMMARY STATISTICS FOR NUMERIC COLUMNS")
    print(df.describe())

    print("\nSUMMARY STATISTICS FOR ALL COLUMNS")
    print(df.describe(include="all"))


def save_scatter_plot(df: pd.DataFrame) -> None:
    """Save a scatter plot showing the relationship between video engagement fields."""
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.scatterplot(
        data=df,
        x="Youtube Views",
        y="Youtube Likes",
        hue="Year",
        size="Estimated Cost",
        sizes=(40, 220),
        alpha=0.75,
        palette="viridis",
        ax=ax,
    )
    plt.title("YouTube Views vs Likes by Super Bowl Year")
    plt.xlabel("YouTube Views (K = thousand, M = million)")
    plt.ylabel("YouTube Likes (K = thousand, M = million)")
    ax.xaxis.set_major_formatter(FuncFormatter(compact_number))
    ax.yaxis.set_major_formatter(FuncFormatter(compact_number))
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "scatter_youtube_views_vs_likes.png", dpi=150)
    plt.close()


def save_histograms(df: pd.DataFrame) -> None:
    """Save histograms for every numeric column to show value distributions."""
    plotting_df = make_plotting_dataframe(df)

    fig, axes = plt.subplots(2, 3, figsize=(13, 9))
    for axis, column in zip(axes.flatten(), plotting_df.columns):
        series = plotting_df[column].dropna()

        if column == "YouTube Views (millions)":
            bins = np.r_[
                np.arange(0, 1.1, 0.1),
                np.arange(2, 11, 1),
                np.arange(25, 201, 25),
            ]
            axis.hist(series, bins=bins, color="#4c78a8", edgecolor="white")
            axis.set_xscale("symlog", linthresh=1)
            axis.set_title("YouTube Views (millions, lower range expanded)")
            axis.set_xlabel("YouTube Views in millions")
            axis.set_xticks([0, 0.1, 0.5, 1, 5, 10, 25, 50, 100, 200])
            axis.set_xticklabels(["0", "0.1", "0.5", "1", "5", "10", "25", "50", "100", "200"])
        else:
            axis.hist(series, bins=20, color="#4c78a8", edgecolor="white")
            axis.set_title(column)
            axis.set_xlabel(column)

        axis.set_ylabel("Number of commercials")

    plt.suptitle("Numeric Feature Distributions with Readable Units", y=1.02)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "histograms_numeric_features.png", dpi=150)
    plt.close()


def save_box_plots(df: pd.DataFrame) -> None:
    """Save box plots for numeric columns to make outliers easier to identify."""
    plotting_df = make_plotting_dataframe(df)
    flierprops = {
        "marker": "D",
        "markerfacecolor": "#d62728",
        "markeredgecolor": "#8c1d18",
        "markersize": 5,
        "alpha": 0.8,
    }

    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    for axis, column in zip(axes.flatten(), plotting_df.columns):
        sns.boxplot(
            x=plotting_df[column],
            ax=axis,
            color="#72b7b2",
            flierprops=flierprops,
        )
        axis.set_title(column)
        axis.set_xlabel(column)

    fig.suptitle("Outlier Check for Numeric Features with Readable Units", y=1.02)
    fig.text(
        0.5,
        0.01,
        "Red diamond markers represent outlier commercials: values much higher or lower than the usual range.",
        ha="center",
        fontsize=10,
    )
    plt.subplots_adjust(bottom=0.12)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "boxplots_numeric_features.png", dpi=150)
    plt.close()


def main() -> None:
    """Run the complete Super Bowl commercials dataset analysis workflow."""
    sns.set_theme(style="whitegrid", context="notebook")
    df = pd.read_csv(DATA_PATH)

    print_dataset_overview(df)
    save_scatter_plot(df)
    save_histograms(df)
    save_box_plots(df)

    print("\nPLOTS SAVED")
    print(OUTPUT_DIR / "scatter_youtube_views_vs_likes.png")
    print(OUTPUT_DIR / "histograms_numeric_features.png")
    print(OUTPUT_DIR / "boxplots_numeric_features.png")


if __name__ == "__main__":
    main()
