import matplotlib.pyplot as plt 
"""
Module for creating bar chart visualizations using penguin dataset.
This module demonstrates basic matplotlib and seaborn functionality for data visualization.
It loads the penguins dataset and creates a titled plot display.
Dependencies:
    - matplotlib.pyplot: For plot creation and display
    - seaborn: For statistical data visualization
    - pandas: For data manipulation and analysis
Functions:
    None (Script execution)
Usage:
    Run the script to display a bar chart with the title "Python"
sns.barplot() Parameters:
    - data: DataFrame or array-like, optional - Input data structure
    - x: str or vector data, optional - Variable name for x-axis or x vector
    - y: str or vector data, optional - Variable name for y-axis or y vector
    - hue: str or vector data, optional - Variable name for color encoding
    - order: list of strings, optional - Order to plot categorical levels
    - hue_order: list of strings, optional - Order for hue levels
    - orient: str, optional - Orientation ('v' for vertical, 'h' for horizontal)
    - color: matplotlib color, optional - Single color for all bars
    - palette: str, list, dict, optional - Color palette for hue variable
    - saturation: float, optional - Proportional saturation (0-1)
    - width: float, optional - Width of bars (0-1)
    - dodge: bool, optional - Whether to dodge bars by hue
    - ci: float, int, or 'sd', optional - Confidence interval size
    - ax: matplotlib Axes, optional - Axes object to plot on
    - errwidth: float, optional - Thickness of error bar lines
    - capsize: float, optional - Width of error bar caps
"""

import seaborn as sns

import pandas as pd 



var=sns.load_dataset("penguins")

# bins=[170,180,190,200,210,220,230,240],
# sns.barplot(x=var.island,y=var.bill_length_mm)
# hue_order=["Female","Male"],ci=50,n_boot=2,palette="cividis",saturation=0.3,errcolor="r",capsize=0.3,dodge=False
o=["Dreams","Torgersen","Biscoe"]

sns.set(style="darkgrid")
sns.barplot(x="island",y="bill_length_mm",data=var,hue="sex",)
# plt.grid()
plt.title("Python")  
plt.show()