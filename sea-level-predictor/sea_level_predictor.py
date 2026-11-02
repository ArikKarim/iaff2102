import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from pathlib import Path
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv(Path(__file__).with_name('epa-sea-level.csv'))


    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    fit = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = np.arange(df['Year'].min(), 2051)
    ax.plot(years, fit.intercept + fit.slope * years, label='1880 onward', color='red')


    # Create second line of best fit
    recent = df.loc[df['Year'] >= 2000]
    recent_fit = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])
    recent_years = np.arange(2000, 2051)
    ax.plot(
        recent_years, recent_fit.intercept + recent_fit.slope * recent_years,
        label='2000 onward', color='green',
    )


    # Add labels and title
    ax.set(title='Rise in Sea Level', xlabel='Year', ylabel='Sea Level (inches)')
    ax.legend()
    fig.tight_layout()


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
