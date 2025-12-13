import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([5,4,3,2,1])

plt.plot(x,y,color="r")


plt.title("Linear Plot")
plt.savefig("./ML/Phase1/Matplotlib/SaveFig.png",dpi=2000,facecolor="g",transparent=False,bb_inches="tight")

plt.show()