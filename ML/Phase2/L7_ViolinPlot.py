import seaborn as sns
"""
Violin Plot Visualization Module
This module demonstrates the creation of violin plots using Seaborn to visualize
the distribution of numerical variables across different categories.
Dataset:
    - Uses the 'tips' dataset from Seaborn containing information about restaurant tips
Main Parameters for sns.violinplot():
    - data: DataFrame or array-like, input data structure
    - x: str, column name for categorical variable on x-axis
    - y: str, column name for numerical variable on y-axis
    - hue: str, column name for grouping/coloring by another categorical variable
    - split: bool, split the violin plot when hue is used (default: False)
    - orient: str, orientation of plot - 'v' (vertical, default) or 'h' (horizontal)
    - palette: str or dict, color palette for the plot
    - inner: str, representation of data inside violin - 'box', 'quartile', 'point', 'stick', or None
    - cut: float, extend the range of the KDE past extreme datapoints (default: 2)
    - scale: str, method for scaling violin widths - 'area', 'count', 'width' (default: 'area')
    - scale_hue: bool, scale the violin width by the number of observations in each bin (default: True)
    - bw: str or float, bandwidth for KDE estimation
    - linewidth: float, width of the lines in the plot
    - saturation: float, color saturation (0 to 1)
    - ax: matplotlib Axes, axes object to draw the plot on
"""


import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

var=sns.load_dataset("tips")

# sns.violinplot(x="day",y="total_bill",data=var,hue="time")
# sns.violinplot(y="day",x="total_bill",data=var,hue="time")

# sns.violinplot(x="time",y="total_bill",data=var,order=["Dinner","Lunch"],inner="quart")


# sns.violinplot(x="time",y="total_bill",hue="sex",data=var,order=["Dinner","Lunch"],split=True,scale="width")

sns.violinplot(y=var["total_bill"])
plt.show()