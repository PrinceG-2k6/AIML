import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([3,1,5,2,4])

plt.plot(x,y,color="r")

# plt.axis([0,10,0,7])


# plt.text(2,5,"Java",fontsize=15,style="italic",bbox={"facecolor":"red"})
# plt.annotate("python",xy=(2,1),xytext=(4,4),arrowprops={"facecolor":"black","shrink":100})


plt.xlabel("Days",fontsize=10)
plt.ylabel("Growth",fontsize=10)
plt.title("Text Example",fontsize=15)
plt.grid()
plt.legend("up",loc=3,facecolor="red",edgecolor="yellow",framealpha=0.3,shadow=True)
plt.show()