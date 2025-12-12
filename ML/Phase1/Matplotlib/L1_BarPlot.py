import matplotlib.pyplot as plt
import numpy as np 

x=["python","C","C++","java"]
y=[100,90,70,80]
z=[20,75,53,20]
p=np.arange(len(x))
width =0.3
p1=[j+width for j in p]

plt.xlabel("Language",fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.title("Price",fontsize=15)

c=["y","r","b","g"]
# plt.bar(x,y,width=0.3,color=c,align="edge",edgecolor="r",linewidth=3,linestyle=":")
plt.bar(p,y,width,color="r",label="popularity1")
plt.bar(p1,z,width,color="y",label="popularity2")

# plt.barh(p,y,width,color="r",label="popularity1")
# plt.barh(p1,z,width,color="y",label="popularity2")


plt.xticks(p+width/2,x,rotation =10)
plt.legend()
plt.show()
