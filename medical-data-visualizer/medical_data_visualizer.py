import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# 1
df = pd.read_csv(Path(__file__).with_name('medical_examination.csv'))

# 2
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# 3
df[['cholesterol', 'gluc']] = (df[['cholesterol', 'gluc']] > 1).astype(int)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df, id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
    )


    # 6
    df_cat = (
        df_cat.groupby(['cardio', 'variable', 'value'])
        .size().reset_index(name='total')
    )


    # 7
    chart = sns.catplot(
        data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar',
        order=sorted(df_cat['variable'].unique()), errorbar=None,
    )


    # 8
    fig = chart.figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[
        (df['ap_lo'] <= df['ap_hi'])
        & df['height'].between(df['height'].quantile(0.025), df['height'].quantile(0.975))
        & df['weight'].between(df['weight'].quantile(0.025), df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))


    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15
    sns.heatmap(
        corr, mask=mask, annot=True, fmt='.1f', center=0,
        vmax=0.3, square=True, linewidths=0.5, cbar_kws={'shrink': 0.5}, ax=ax,
    )
    fig.tight_layout()


    # 16
    fig.savefig('heatmap.png')
    return fig
