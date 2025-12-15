import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

# sns.pairplot() parameters:
# data: DataFrame - the input data
# hue: str - column name for color encoding
# palette: str or dict - color palette
# diag_kind: str - plot type for diagonal ('auto', 'hist', 'kde')
# plot_kws: dict - keyword arguments for off-diagonal plots
# diag_kws: dict - keyword arguments for diagonal plots
# kind: str - plot type ('scatter', 'kde', 'hist', 'reg')
# corner: bool - if True, only plot lower triangle
# dropna: bool - if True, drop NaN values
# height: float - height of each facet
# aspect: float - aspect ratio of each facet
# markers: str or list - marker styles
# x_vars: list - variables for x axis
# y_vars: list - variables for y axis
# vars: list - variables to plot
# corner: bool - if True, plot only lower triangle

var = sns.load_dataset("tips").head(20)
m={
    "Male":"*",
    "Female":"o"
}

sns.pairplot(var,vars=["total_bill","tip"],hue="sex",hue_order=["Female","Male"],markers=m)

# sns.pairplot(var,hue="sex",hue_order=["Female","Male"],x_vars=["total_bill","tip"],kind="hist")



plt.show()