import matplotlib.pyplot as plt 
"""
Module for creating and visualizing histograms using matplotlib and seaborn.
This module demonstrates basic histogram creation with pandas DataFrames
and the seaborn library. It loads sample penguin data and creates visualization
with grid and title formatting.
Functions:
    None - Script contains inline visualization code
Variables:
    var (list): List of integers [1,2,3,4,5,6,7] for first dataset
    var1 (list): List of integers [2,3,4,1,5,6,7] for second dataset
    x1 (pd.DataFrame): DataFrame containing 'var' and 'var1' columns
    var (pd.DataFrame): First 20 rows of the penguins dataset from seaborn
sns.histplot() Parameters:
    data (DataFrame): Input data for plotting
    x (str): Column name for x-axis variable
    y (str): Column name for y-axis variable (optional)
    hue (str): Column name for color-coding by category
    kde (bool): Whether to overlay kernel density estimate
    stat (str): Type of statistic to compute ('count', 'frequency', 'density', 'probability')
    bins (int or sequence): Number of bins or bin edges
    binwidth (float): Width of bins
    palette (str or dict): Color palette for hue variable
    color (str): Single color for bars
    edgecolor (str): Color of bar edges
    linewidth (float): Width of bar edges
    alpha (float): Transparency level (0-1)
    shrink (float): Shrink bars by this fraction
    log_scale (bool): Use log scale
    element ({'bars', 'step', 'poly'}): Type of plot element
    fill (bool): Whether to fill bars
    legend (bool): Show legend
    ax (Axes): Matplotlib axes object
"""
import seaborn as sns

import pandas as pd 


# var =[1,2,3,4,5,6,7]
# var1 =[2,3,4,1,5,6,7]

# x1= pd.DataFrame({
#     "var":var,
#     "var1":var1
# })
var=sns.load_dataset("penguins")

# bins=[170,180,190,200,210,220,230,240],
sns.displot(var["flipper_length_mm"],kde=True,rug=True,color="r",log_scale=True)
# plt.grid()
plt.title("Python")
plt.show()