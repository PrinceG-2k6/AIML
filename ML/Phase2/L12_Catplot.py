import seaborn as sns
"""
Catplot visualization script for tips dataset analysis.
This module demonstrates the usage of seaborn's catplot function for categorical
data visualization. It loads the tips dataset and prepares marker mapping for
different gender categories.
Dataset:
    - tips: A dataset containing information about restaurant tips, including
            attributes like sex, day, time, total_bill, tip, etc.
Marker Mapping:
    - Male: 'o' (circle marker)
    - Female: '<' (left-pointing triangle marker)
sns.catplot() Parameters:
    - data: DataFrame containing the data to plot
    - x: Column name for x-axis variable (categorical)
    - y: Column name for y-axis variable (numeric)
    - hue: Column name for color encoding by category
    - col: Column name for faceting subplots horizontally
    - row: Column name for faceting subplots vertically
    - kind: Type of plot ('strip', 'swarm', 'box', 'violin', 'boxen', 'point', 'bar', 'count')
    - height: Height of each subplot (default: 5)
    - aspect: Aspect ratio of each subplot (default: 1)
    - palette: Color palette to use
    - markers: Marker styles for 'point' or 'strip' plots
    - dodge: Whether to dodge points along categorical axis
    - jitter: Amount of jitter for strip/swarm plots
    - order: Order of categorical values on x-axis
    - hue_order: Order of categorical values for hue
    - col_order: Order of column facets
    - row_order: Order of row facets
    - size: Size of plot elements
    - sizes: Range for marker sizes when size is used
    - style: Column name for style encoding
    - style_order: Order of style values
"""

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

var = sns.load_dataset("tips").head(20)

m={
    "Male":"o",
    "Female":"<"
}

sns.catplot(x="day",y="size",data=var,hue="sex",height=10,kind="boxen")

plt.show()