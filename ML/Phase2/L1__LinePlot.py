import matplotlib.pyplot as plt 
import seaborn as sns
"""
This script imports the necessary libraries for data visualization using 
Matplotlib and Seaborn. 

Modules:
- matplotlib.pyplot: A collection of functions that make Matplotlib work like 
    MATLAB, providing a MATLAB-like interface for plotting.
- seaborn: A statistical data visualization library based on Matplotlib that 
    provides a high-level interface for drawing attractive and informative 
    statistical graphics.

Usage:
- This script is intended to be used for creating line plots using Seaborn's 
    lineplot function.

Parameters for sns.lineplot():
- data: (DataFrame or array-like) The data to be plotted.
- x: (string or int) The name of the variable in data to be plotted on the x-axis.
- y: (string or int) The name of the variable in data to be plotted on the y-axis.
- hue: (string) Grouping variable that will produce different colors for 
    different levels of the variable.
- style: (string) Grouping variable that will produce different styles for 
    different levels of the variable.
- size: (string) Grouping variable that will produce different sizes for 
    different levels of the variable.
- palette: (string, list, or dict) Colors to use for the different levels of 
    the hue variable.
- markers: (bool or list) Marker styles for different levels of the style variable.
- dashes: (bool or list) Dash styles for different levels of the style variable.
- estimator: (callable) A function that will be used to estimate the value of 
    the y variable at each x value.
- errorbar: (string or bool) The method to use for computing the error bars.
- ci: (int or "sd") The size of the confidence interval to draw around the 
    estimated values.
- n_boot: (int) The number of bootstrap iterations to use when computing 
    confidence intervals.
- sort: (bool) Whether to sort the data before plotting.
- ax: (matplotlib.axes.Axes) The axes on which to plot.
- **kwargs: Additional keyword arguments passed to the underlying matplotlib 
    functions.
"""
import pandas as pd 
var =[1,2,3,4,5,6,7]
var1 =[2,3,4,1,5,6,7]

x1= pd.DataFrame({
    "var":var,
    "var1":var1
})
y1=sns.load_dataset("penguins")


# plt.plot(var,var1)
# sns.lineplot(var,var1)
# sns.lineplot(x="var",y="var1",data=x1)

# print(y1)

sns.lineplot(x="bill_length_mm",y="bill_depth_mm",data=y1,hue="sex",style="sex",palette="Accent",markers=["o",">"])


plt.show()