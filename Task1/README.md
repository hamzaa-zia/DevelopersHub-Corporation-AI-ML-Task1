# Super Bowl Commercials Dataset Analysis

This project analyzes the `superbowl_commercials.csv` dataset using Python. The script loads the data, prints basic dataset summaries, and creates three visualizations: a scatter plot, histograms, and box plots.

The dataset is taken from the Maven Analytics website. OpenAI Codex was used to help build and refine the project, and the analysis can be run in Jupyter Notebook in the browser through Anaconda Navigator.

## Libraries Used

### pandas

`pandas` is used for loading and exploring the dataset.

Main functions used:

- `pd.read_csv()` loads the CSV file into a DataFrame.
- `.shape` shows the number of rows and columns.
- `.columns` lists all column names.
- `.head()` displays the first few rows.
- `.info()` shows column data types, missing values, and memory usage.
- `.describe()` gives summary statistics such as mean, minimum, maximum, and quartiles.
- `.select_dtypes()` selects only numeric columns for plotting.

### matplotlib

`matplotlib` is used to create figures, label charts, and save plots as image files.

Main functions used:

- `plt.subplots()` creates figure and axis layouts.
- `plt.title()`, `plt.xlabel()`, and `plt.ylabel()` label the charts.
- `plt.tight_layout()` improves spacing so labels do not overlap.
- `plt.savefig()` saves each visualization as a PNG file.
- `plt.close()` closes the chart after saving.

### seaborn

`seaborn` is used to create cleaner statistical visualizations on top of matplotlib.

Main functions used:

- `sns.set_theme()` applies a clean visual style.
- `sns.scatterplot()` creates the relationship plot between views and likes.
- `sns.boxplot()` creates box plots for outlier detection.

### numpy

`numpy` is used to create custom bin ranges for the YouTube Views histogram.

Main functions used:

- `np.arange()` creates numeric ranges for histogram bins.
- `np.r_[]` combines multiple bin ranges into one list of bin edges.

This is useful because YouTube views are unevenly distributed. Most commercials have lower view counts, while a few have extremely high views.

### matplotlib.ticker.FuncFormatter

`FuncFormatter` is used to make large numbers easier to read on chart axes.

For example:

- `250000` becomes `250K`
- `1000000` becomes `1M`

This helps viewers understand YouTube views and likes without guessing the scale.

## Workflow

1. The script loads the CSV file from:

   ```text
   E:\Internship\Super+Bowl+Commercials\superbowl_commercials.csv
   ```

2. It prints the dataset shape, column names, first five rows, dataset information, and summary statistics.

3. It creates readable plotting columns for large values:

   ```python
   "YouTube Views (millions)": df["Youtube Views"] / 1_000_000
   "YouTube Likes (thousands)": df["Youtube Likes"] / 1_000
   ```

   The original dataset is not changed. These simplified columns are only used to make the charts easier to understand.

4. It saves three visualization files:

   ```text
   scatter_youtube_views_vs_likes.png
   histograms_numeric_features.png
   boxplots_numeric_features.png
   ```

## Visualization 1: Scatter Plot

The scatter plot compares `Youtube Views` and `Youtube Likes`.

Each point represents one Super Bowl commercial.

- The x-axis shows YouTube views.
- The y-axis shows YouTube likes.
- Color represents the Super Bowl year.
- Point size represents estimated commercial cost.

This visualization helps show whether commercials with more views also tend to receive more likes. It can also reveal unusually popular commercials that stand far away from the main group.

What can be observed:

- Ads with very high views are easy to spot.
- A positive relationship may appear if higher views generally come with higher likes.
- Some ads may have many views but relatively fewer likes, which can suggest weaker engagement.

## Visualization 2: Histograms

Histograms show the distribution of numeric values.

Instead of showing every row one by one, the histogram groups values into ranges called bins. The height of each bar shows how many commercials fall into that range.

The `YouTube Views` histogram uses custom bins and a lightly adjusted x-axis. The lower range from 0 to 1 million views is given more space because most commercials are concentrated there. Higher view counts are still included, but they are grouped into wider ranges so they do not make the lower-view commercials look like one single bar.

This visualization helps answer questions like:

- Are most commercials short or long?
- Are most YouTube view counts low, medium, or high?
- Are estimated costs usually similar or spread out?
- Are most commercials from certain years?

What can be observed:

- Most values usually cluster in certain ranges.
- Very large values may appear as long tails.
- YouTube views and likes can be uneven because a few commercials may become much more popular than others.

## Visualization 3: Box Plots

Box plots summarize numeric features and help identify outliers.

In each box plot:

- The middle line shows the median.
- The box shows the middle 50% of values.
- The whiskers show the usual low and high range.
- Red diamond markers show outlier commercials.

The red diamonds are values that are much higher or lower than the normal range for that feature. For example, a commercial with extremely high YouTube views may appear as a red diamond.

This visualization helps answer questions like:

- Which features have unusual values?
- Are there commercials with extremely high views or likes?
- Are most values tightly grouped or widely spread out?

What can be observed:

- YouTube views and likes may have strong outliers.
- Length can reveal unusually long commercials.
- Estimated cost can show whether some commercials were much more expensive than typical ads.

## How to Run

Run this command from the project folder:

```powershell
python .\superbowl_commercials_analysis.py
```

After running, the script prints the dataset summary in the terminal and saves the visualization images in the same folder as the script.
