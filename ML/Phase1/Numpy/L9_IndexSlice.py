import numpy as np

"""
        [1,     2,   3,     4]
index    0,     1,   2,     3
reverse  -4,    -3, -2,     -1   
"""

# INDEXING

# var = np.array([1,2,3,4,5,6,7])
# print(var[0])
# print(var[-2])

# var1 = np.array([[1,2,3,4],
#                  [5,6,7,8]])
# # print(var1[0])
# # print(var1[-2])
# print(var1[0,2])
# print(var1[-2,2])


# SLICING
# var1 = np.array([[1,2,3,4],
#                  [5,6,7,8]])
# # print(var1[start:stop:skip])
# print(var1[0: , 1:4:2])
# print(var1[0: , 0:4:2]) 

var = np.array([1,2,3,4,5,6,7])
print(var[0:6:2])
print(var[-2:])

