import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([4,1,3,5,2])

plt.plot(x,y,color="r")
# plt.fill_between(x=[2,4],y1=2,y2=4)
plt.fill_between(x,y,where=(x>=2) & (x<=4),alpha=0.5)
plt.show()