import seaborn as sns
"""
This script sets up a basic structure for creating a strip plot using Seaborn.
Imports:
- seaborn: for creating statistical graphics.
- matplotlib.pyplot: for plotting.
- pandas: for data manipulation and analysis.
- numpy: for numerical operations.
Parameters for sns.stripplot():
- data: DataFrame or array-like, the data to be plotted.
- x: name of the variable in data or vector data, the variable to be plotted on the x-axis.
- y: name of the variable in data or vector data, the variable to be plotted on the y-axis.
- hue: name of the variable in data or vector data, used for color encoding.
- order: order of categories for the x-axis.
- jitter: boolean or float, whether to add jitter to the points.
- dodge: boolean, whether to separate points for different levels of the hue variable.
- marker: string, the marker style for the points.
- size: scalar or array-like, the size of the points.
- ax: matplotlib Axes, the axes to plot on.
- **kwargs: additional keyword arguments passed to matplotlib.
"""
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np


var = sns.load_dataset("tips")

m={
    "Male":"o",
    "Female":"<"
}

# sns.stripplot(x="day",y="total_bill",data=var,hue="sex",jitter=1,marker="<")

sns.stripplot(y="total_bill",data=var)

plt.show()