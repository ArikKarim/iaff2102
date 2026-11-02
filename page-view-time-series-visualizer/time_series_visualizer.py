import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from calendar import month_name, month_abbr
from pathlib import Path
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
    Path(__file__).with_name('fcc-forum-pageviews.csv'),
    parse_dates=['date'], index_col='date',
)

# Clean data
df = df.loc[df['value'].between(df['value'].quantile(0.025), df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df_line.index, df_line['value'], color='firebrick', linewidth=1)
    ax.set(
        title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
        xlabel='Date', ylabel='Page Views',
    )
    fig.tight_layout()


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack('month')

    # Draw bar plot
    ax = df_bar.plot.bar(figsize=(12, 8))
    fig = ax.figure
    ax.set(xlabel='Years', ylabel='Average Page Views')
    ax.legend(title='Months', labels=list(month_name)[1:])
    fig.tight_layout()


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(20, 7))
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
    sns.boxplot(
        data=df_box, x='month', y='value', order=list(month_abbr)[1:], ax=axes[1],
    )
    axes[0].set(title='Year-wise Box Plot (Trend)', xlabel='Year', ylabel='Page Views')
    axes[1].set(title='Month-wise Box Plot (Seasonality)', xlabel='Month', ylabel='Page Views')
    fig.tight_layout()


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
