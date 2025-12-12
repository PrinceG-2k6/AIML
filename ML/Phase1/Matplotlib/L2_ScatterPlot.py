import matplotlib.pyplot as plt

Day =[1,2,3,4,5,6,7]
no=[2,3,1,4,5,3,6]
no2=[1,6,3,2,2,3,6]
size = [1000,200,400,500,1000,700,400]
colors = [10,48,29,96,92,85,66]
plt.scatter(Day,no,c = colors,s=size,alpha=0.8,marker="*",edgecolors="g",linewidths=1,cmap="BrBG")
plt.scatter(Day,no2,c = colors,s=size)
t=plt.colorbar()
t.set_label("Color_Bar",fontsize=15)
plt.title("ScatterPlot",fontsize=10)
plt.xlabel("Day",fontsize=10)
plt.ylabel("No..",fontsize=10)
plt.show()