import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([1,2,3,4,5])

plt.subplot(2,2,1)
plt.plot(x,y,color="r")

plt.subplot(2,2,2)
plt.pie([1],colors="b")

plt.subplot(2,2,3)
x1=[10,20,30,40]
plt.pie(x1)

plt.subplot(2,2,4)
x2=["a","s","d","f"]
y2=[10,20,30,40]
plt.bar(x2,y2)

plt.show()