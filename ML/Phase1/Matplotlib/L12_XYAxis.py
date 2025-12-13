import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([1,2,3,4,5])

plt.plot(x,y,color="r")

# plt.xticks(x,labels=["A","B","C","D","E"])
# plt.yticks(y)

# plt.xlim(0,10)
# plt.ylim(0,10)

plt.axis([0,10,0,7])

plt.grid()
plt.show()