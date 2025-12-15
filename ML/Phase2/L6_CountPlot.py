import seaborn as sns
"""
Module for creating count plots and visualizing categorical data distributions.
This module provides functionality for:
- Creating count plots using seaborn
- Visualizing the frequency of categorical variables
- Customizing plot appearance with matplotlib
Dependencies:
    - seaborn: Statistical data visualization library
    - matplotlib.pyplot: Plotting library for creating visualizations
    - pandas: Data manipulation and analysis library
    - numpy: Numerical computing library
sns.countplot() Parameters:
    - data: DataFrame or array-like, optional. Dataset for plotting
    - x: str or vector data, optional. Variable name or data for x-axis
    - y: str or vector data, optional. Variable name or data for y-axis
    - hue: str, optional. Variable name for grouping and coloring by category
    - order: list of strings, optional. Order to plot categorical levels
    - hue_order: list of strings, optional. Order for hue levels
    - orient: str, optional. Orientation of plot ('v' for vertical, 'h' for horizontal)
    - color: matplotlib color, optional. Single color for all bars
    - palette: palette name or dict, optional. Color palette for the plot
    - ax: matplotlib axes, optional. Axes object to draw the plot onto
    - kwargs: Additional keyword arguments passed to matplotlib.patches.Rectangle
"""

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np


var=sns.load_dataset("tips")

# sns.barplot(x="sex",y="size",data=var)#See the differnce


# sns.countplot(y="sex",data=var,hue="smoker")
sns.countplot(x="sex",data=var,hue="smoker",palette="cividis",saturation=0.9)#Count of male and female


plt.show()