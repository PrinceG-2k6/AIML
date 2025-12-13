import matplotlib.pyplot as plt


x=[1,2,3,4,5]
y=[4,1,3,5,2]


plt.step(x,y,color="r",marker="o",ms=10,mfc="g",label="Pyhton")

plt.grid()
plt.title("StepPlot")
plt.xlabel("X axis")
plt.ylabel("Y axis")


plt.legend()
plt.show()