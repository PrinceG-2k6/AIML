import seaborn as sns
"""
Box Plot Visualization Module
This module demonstrates the creation of box plots using Seaborn and Matplotlib.
It includes a marker mapping dictionary for different gender categories.
Module Components:
    - Marker mapping dictionary for visualizing data by gender categories
    - sns.boxplot() parameters reference for customization
sns.boxplot() Parameters:
    - data: DataFrame or array-like, input data structure
    - x: str, name of the variable for x-axis positioning
    - y: str, name of the variable for y-axis positioning
    - hue: str, variable in data to map plot aspects by color
    - order: list, order in which categories should appear on axis
    - hue_order: list, order for hue variable categories
    - orient: str, orientation of the plot ('v' for vertical, 'h' for horizontal)
    - color: matplotlib color, single color for all elements
    - palette: str or dict, color palette for the plot
    - width: float, width of box plot elements (0 to 1)
    - dodge: bool, whether to separate hue levels along the axis
    - fliersize: int, size of outlier points
    - linewidth: float, width of lines in box plot elements
    - ax: matplotlib axes, axes object to draw the plot
    - kwargs: additional keyword arguments for styling
"""

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np


var = sns.load_dataset("tips")

m={
    "Male":"o",
    "Female":"<"
}

sns.set(style="whitegrid")

sns.boxplot(x="day",y="total_bill",data=var,color="r",showmeans=True,meanprops={"marker":"+","markeredgecolor":"b"},palette="plasma")

plt.show()