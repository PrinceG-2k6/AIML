import matplotlib.pyplot as plt
"""
Module for demonstrating matplotlib stacked area plots.
This module provides functionality to create stacked area plots using matplotlib.
Stacked area plots are useful for visualizing how multiple data series contribute
to a total over time or across categories.
Key functions from matplotlib.pyplot used:
    - plt.stackplot(): Creates a stacked area plot
      Parameters:
        - x: The x-coordinates of the data points (array-like)
        - *args: Variable number of y-coordinate arrays for each data series
        - baseline: Type of baseline for stacking ('zero', 'sym', 'wiggle', 'weighted_wiggle')
        - labels: Sequence of strings for legend labels (optional)
        - colors: Sequence of colors for each area (optional)
        - alpha: Transparency level for the areas, value between 0-1 (optional)
        - interpolate: Boolean to enable interpolation between points (optional)
        - step: Type of step function ('pre', 'post', 'mid') for step-like stacks (optional)
Example use cases:
    - Visualizing cumulative contributions over time
    - Displaying composition of data across multiple categories
    - Analyzing trends in stacked components
"""

x=[1,2,3,4,5]
area1=[3,1,2,4,5]
area2=[4,2,6,3,1]
area3=[2,1,3,4,5]

l= ["area1",'area2',"area3"]
c = ["r","g","m"]
plt.stackplot(x,area1,area2,area3,labels=l,colors=c,baseline="wiggle")

plt.grid()
plt.legend(loc=2)
plt.show()
