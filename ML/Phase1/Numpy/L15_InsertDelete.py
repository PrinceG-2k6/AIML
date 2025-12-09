import numpy as np

var =np.array([1,2,3,4,5])

var=np.insert(var,1,4.5)
var = np.append(var,999)

print(var)

var1 = np.array([[1,2,3,4],[5,6,7,8]])
# var1 = np.insert(var1,(1,2),[9,0,0,9],axis=0)

# var1 = np.insert(var1,(1,2),9,axis=1)

var1 = np.append(var1,[[45,44,43]],axis=0)
print(var1)