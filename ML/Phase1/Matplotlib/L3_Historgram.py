import matplotlib.pyplot as plt

import numpy as np
import random

x =np.random.randint(10,60,(50))

l = [10,20,30,40,50,60]
plt.hist(x,color="r",edgecolor="b",bins=l,cumulative=-1,bottom=10,align="mid",orientation="vertical",rwidth=0.6,log=True,label="Python")


plt.title("HistorGram")
plt.xlabel("Pyhotn")
plt.ylabel("No..")
plt.legend()
plt.axvline(45,color="g",label="line")
plt.grid()
plt.show()