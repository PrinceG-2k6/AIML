import seaborn as sns
"""
Module for creating scatter plots using Seaborn and Matplotlib.

This module provides functionality to visualize relationships between variables
using scatter plots. It leverages Seaborn for statistical visualization,
Matplotlib for low-level plotting control, and Pandas for data manipulation.

Dependencies:
    - seaborn: Statistical data visualization library
    - matplotlib.pyplot: Plotting library for creating visualizations
    - pandas: Data manipulation and analysis library

Common sns.scatterplot() parameters:
    - data: DataFrame or None - Input data structure
    - x: str or array-like - Column name or data for x-axis
    - y: str or array-like - Column name or data for y-axis
    - hue: str or None - Column name for color encoding
    - size: str or None - Column name for marker size encoding
    - style: str or None - Column name for marker style encoding
    - palette: str, list, or dict - Color palette for hue variable
    - sizes: dict or tuple - Range of marker sizes
    - markers: dict or str - Marker styles for style variable
    - alpha: float - Transparency level (0-1)
    - ax: matplotlib axes object - Axes to plot on
    - height: float - Figure height (when using FacetGrid)
    - aspect: float - Aspect ratio of plot
    - legend: bool or str - Show/hide or place legend
"""
import matplotlib.pyplot as plt 
import pandas as pd 



var=sns.load_dataset("penguins").head(20)
m={
    "Male":"*",
    "Female":"o"
}
sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",data=var,hue="sex",style="sex",size="sex",sizes=(100,40),palette="Accent",alpha=1,markers=m)



plt.show()