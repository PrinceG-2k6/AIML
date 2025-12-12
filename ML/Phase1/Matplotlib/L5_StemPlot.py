import matplotlib.pyplot as plt
"""
Matplotlib Stem Plot Module (L5_StemPlot.py)

This module demonstrates the creation and customization of stem plots using matplotlib.pyplot.
Stem plots are useful for visualizing discrete data points connected to a baseline.

plt.stem() Parameters:
    - x (array-like): x-axis values/positions for the stem points
    - y (array-like): y-axis values for the stem points
    - linefmt (str): format string for the stem lines (e.g., 'r-', 'b--')
    - markerfmt (str): format string for the markers at stem tops (e.g., 'ro', 'bs')
    - basefmt (str): format string for the baseline (e.g., 'k-', 'gray')
    - bottom (float): y-position of the baseline (default: 0)
    - label (str): label for the stem plot in the legend
"""
x = [1,2,3,4,5,6]
y=[2,2,5,6,7,3]

plt.stem(x,y,linefmt=":",markerfmt="r+",bottom=4,basefmt="g",label="Pyhton",orientation="horizontal")
plt.legend()
plt.show()