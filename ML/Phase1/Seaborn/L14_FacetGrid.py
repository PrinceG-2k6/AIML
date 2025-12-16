import seaborn as sns
"""
FacetGrid visualization module for exploring the tips dataset.
This module demonstrates the use of Seaborn's FacetGrid to create multi-plot grids
for conditional data visualization. It loads the tips dataset and prepares marker
mappings for different categories.
Module Setup:
    - Loads the "tips" dataset from Seaborn
    - Defines marker styles for categorical data (Male: circle, Female: left triangle)
sns.FacetGrid() Parameters:
    - data: DataFrame containing the dataset to plot
    - col: Column name for faceting into columns
    - row: Column name for faceting into rows
    - col_wrap: Number of columns to wrap at (when using col without row)
    - hue: Column name for color encoding
    - palette: Color palette (string name or dict mapping)
    - height: Height of each facet in inches
    - aspect: Aspect ratio of each facet (width/height)
    - col_order: Order of column facets
    - row_order: Order of row facets
    - hue_order: Order of hue categories
    - margin_titles: Boolean to place titles on the margins
    - despine: Boolean to remove spines
    - dropna: Boolean to drop NA values
    - size: (deprecated) use height instead
    - xlim: X-axis limits
    - ylim: Y-axis limits
"""
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

var = sns.load_dataset("tips")

m={
    "Male":"o",
    "Female":"<"
}

fg = sns.FacetGrid(var,col="sex",hue="day")
fg.map(plt.scatter,"total_bill","tip").add_legend()


plt.show()