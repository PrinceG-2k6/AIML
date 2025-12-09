import numpy as np

# SHAPE

# var = np.array([[1,2],[2,3]])
# print(var)
# print(var.shape)

# var1 = np.array([1,2,3,4],ndmin=4)
# print(var1)
# print(var1.shape)

# RESHAPE

var = np.array([1,2,3,4,5,6,7,8])
x =var.reshape(2,2,2)
# x=var.reshape(2,4)
print(x)
print(x.shape)

print()

x = x.reshape(-1)#Converts to 1D
print(x)
print(x.shape)
