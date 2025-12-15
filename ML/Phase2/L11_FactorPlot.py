import seaborn as sns
"""
This module demonstrates the creation of factor plots using Seaborn.
It initializes a marker mapping dictionary for visualizing categorical data
by gender (Male and Female with different marker styles), and is set up to
display matplotlib plots.
Typical usage would involve calling sns.factorplot() with the following parameters:
    - data: DataFrame containing the data to plot
    - x: Column name for x-axis variable
    - y: Column name for y-axis variable
    - hue: Column name for color encoding by category
    - col: Column name for faceting by columns
    - row: Column name for faceting by rows
    - kind: Type of plot ('point', 'bar', 'strip', 'swarm', 'box', 'violin', 'count', 'bar')
    - height: Height of each facet (default: 5)
    - aspect: Aspect ratio of each facet (default: 1)
    - col_wrap: Wrap column facets at this width
    - palette: Color palette for hue variable
    - markers: Dictionary or list of marker styles
    - style: Column name for line style encoding
    - size: Column name for marker size encoding
    - sizes: Range of marker sizes as tuple
    - legend: Whether to include legend (default: True)
    - ci: Size of confidence interval (default: 95)
    - dodge: Whether to shift overlapping points (default: True)
"""
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

var = sns.load_dataset("tips")

m={
    "Male":"o",
    "Female":"<"
}

sns.factorplot(x="size",y="tip",data=var)

plt.show()