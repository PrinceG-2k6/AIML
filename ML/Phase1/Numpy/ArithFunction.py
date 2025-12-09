import numpy as np

# np.mmin(x)
# np.max(x)
# np.argmin(x)
# np.sqrt(x)
# np.sin(x)
# np.cos(x)
# np.cumsum(z)

# axis =0  Column
# axis =1 Row Default

# var = np.array([1,2,3,4,5,6,7,8,9])
# print(np.min(var))
# print(np.max(var))
# print(np.argmin(var))
# print(np.argmax(var))
# print(np.sqrt(var))
# print(np.cumsum(var))

var1 = np.array([[1,6,7,4],
                 [5,2,3,8]])
print(np.min(var1,axis=0))#Column
print(np.min(var1,axis=1))#Row
print(np.sqrt(var1))