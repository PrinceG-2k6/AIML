import matplotlib.pyplot as plt
"""
Module for creating and visualizing pie charts using Matplotlib.
This module provides functionality to generate pie plot visualizations
with customizable styling and formatting options.
plt.pie() parameters:
    - x (sequence): The sizes of the pie slices.
    - labels (sequence, optional): Sequence of strings providing the labels for each wedge.
    - colors (sequence, optional): A sequence of colors for each wedge.
    - autopct (str or callable, optional): Format string or function to display percentages on slices.
    - startangle (float, optional): Rotation of the pie chart in degrees (default: 0).
    - explode (sequence, optional): Offsets (in fractions) for each wedge.
    - shadow (bool, optional): Whether to draw a shadow beneath the pie chart (default: False).
    - textprops (dict, optional): Dictionary of text properties for labels.
    - wedgeprops (dict, optional): Dictionary of properties for wedges.
    - center (tuple, optional): Center position of the pie chart (default: (0, 0)).
    - radius (float, optional): Radius of the pie chart (default: 1).
    - counterclock (bool, optional): Whether to draw slices counterclockwise (default: False).
    - frame (bool, optional): Whether to draw a frame around the pie chart (default: False).
"""

import numpy as np
import random

# x = [10,20,30,40]
# y=["C","C++","Java","Pyhton"]
# ex = [0.4,0.0,0.2,0.0]
# plt.pie(x,labels=y,explode=ex,autopct="%0.2f%%",shadow=True,radius=1.5,labeldistance=1.1,startangle=90,textprops={"fontsize":15},counterclock=False,wedgeprops={"linewidth":4,"edgecolor":"m"},)

# plt.title("PieChart")
# plt.legend()

# plt.show()


