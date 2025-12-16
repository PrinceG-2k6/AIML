import seaborn as sns

import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

"""
Penguin Dataset Visualization - Scatter Plot with Seaborn
This script loads the penguins dataset and creates a scatter plot visualization
showing the relationship between bill length and bill depth, with different
markers and colors based on penguin sex.
Dependencies:
    - seaborn: Statistical data visualization library
    - matplotlib: Plotting library
    - pandas: Data manipulation and analysis library
Dataset:
    - Source: seaborn built-in dataset "penguins"
    - Records: First 20 rows
    - Key columns: bill_length_mm, bill_depth_mm, sex
Visualization Parameters:
    - X-axis: bill_length_mm (bill length in millimeters)
    - Y-axis: bill_depth_mm (bill depth in millimeters)
    - Hue: sex (color differentiation by sex)
    - Style: sex (marker shape by sex)
    - Size: sex (marker size by sex)
    - Markers: Custom mapping (Male="*", Female="o")
    - Sizes: Range (100, 40) for marker sizes
    - Palette: "Accent" color palette
    - Alpha: 1 (full opacity)
sns.heatmap() Common Parameters (for reference):
    - data: Input 2D dataset (DataFrame or array)
    - vmin/vmax: Colormap value range
    - cmap: Colormap name
    - center: Center value for diverging colormaps
    - annot: Display values in cells (True/False)
    - fmt: String formatting for annotations
    - linewidths: Width of lines separating cells
    - cbar: Show colorbar (True/False)
    - cbar_kws: Colorbar customization dictionary
    - square: Make cells square (True/False)
    - robust: Use median/percentiles instead of min/max
    - ax: Matplotlib axes object
"""

y={"fontsize":10,
   "color":"r"
   }


var = np.linspace(1,10,20).reshape(4,5)
v=sns.heatmap(var,vmin=0,vmax=10,cmap="PuOr",annot=True,annot_kws=y,linewidths=12,linecolor="y",cbar=False,xticklabels=False,yticklabels=False)

v.set(xlabel="Python",ylabel="Prince")
sns.set(font_scale=1)

# var = np.linspace(1,10,10).reshape(2,5)
# ar=np.array([["a0","a1","a2","a3","a4"],["b0","b1","b2","b3","b4"]])
# sns.heatmap(var,vmin=0,vmax=10,cmap="PuOr",annot=ar,fmt="s")


# d=sns.load_dataset("anagrams")
# x=d.drop(columns=["attnr"],axis=1).head(10)
# # print(x)

# sns.heatmap(x)
plt.show()