import numpy as np

# # var1 = np.array([1,2,3,4])
# # var2=np.array([5,6,7,8])

# # ar = np.concatenate((var1,var2))


# var1 = np.array([[1,2],[3,4]])
# var2=np.array([[5,6],[7,8]])

# # ar = np.concatenate((var1,var2),axis=0) COLUMN

# # ar = np.concatenate((var1,var2),axis=1) ROW
# # ar = np.hstack((var1,var2))
# # ar = np.vstack((var1,var2))
# ar = np.dstack((var1,var2))
# print(ar)

# SPLIT
# var = np.array([1,2,3,4,5,6])
# print(var)
# ar = np.split(var,2)
# print()
# print(ar)

# ar = np.split(var,3)
# print()
# print(ar)
# print(ar[0])

var = np.array([[1,2,3,4],[5,6,7,8]])
ar = np.array_split(var,2,axis=0)
print(ar)
ar = np.array_split(var,2,axis=1)
print(ar)