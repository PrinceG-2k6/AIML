import matplotlib.pyplot as plt
"""
Generate a box plot visualization using Matplotlib.
This script creates a simple box plot to display the distribution of data points.
The box plot shows the quartiles, median, and outliers of the dataset.
plt.boxplot() Parameters:
    - x: Sequence of arrays/data to plot (required) - list or array of values
    - notch: bool, optional (default=False) - If True, creates notched boxes
    - sym: str, optional - Marker style for outliers (default='b+')
    - vert: bool, optional (default=True) - Vertical (True) or horizontal (False) orientation
    - patch_artist: bool, optional (default=False) - If True, returns filled box patches
    - widths: float or sequence, optional - Width(s) of boxes relative to bin width
    - labels: sequence, optional - Labels for each dataset
    - positions: sequence, optional - Positions of boxes
    - showmeans: bool, optional (default=False) - Show arithmetic mean as a point
    - meanline: bool, optional (default=False) - Display mean as a line
    - showcaps: bool, optional (default=True) - Show the caps at the ends of whiskers
    - showbox: bool, optional (default=True) - Show the box outline
    - showfliers: bool, optional (default=True) - Show the outliers beyond whiskers
    - whis: float or tuple, optional (default=1.5) - Position of whiskers
    - capwidths: float, optional - Width of whisker caps
    - zorder: scalar, optional - Drawing order
    - manage_ticks: bool, optional - Whether to manage tick positions
"""

x=[10,20,30,40,50,60,70,120]
x1=[50,60,70,120,140,260]
x2=[120,150,200]
y=[x,x1,x2]
# notch=True

plt.boxplot(y,label=["python","C","C++"],patch_artist=True,showmeans=True,whis=2,sym="g+",boxprops={"color":"r"},capprops={"color":"g"},whiskerprops={"color":"y"},flierprops={"markeredgecolor":"m"})
plt.show()