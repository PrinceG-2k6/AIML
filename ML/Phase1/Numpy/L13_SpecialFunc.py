import numpy as np

"""
Search
Sort
"""

# SEARCH

# var = np.array([1,2,3,4,5,6,7,2,5,3,4])
# x = np.where((var%2)==0)
# print(x) 

# var = np.array([0,1,2,3,4,5,6,7])#Sorted Array
# x = np.searchsorted(var,5)#inarySearch leftToRight
# x = np.searchsorted(var,5,side="right")#inarySearch RightToLeft
# print(x)


# SORT

# # var = np.array([7,2,5,3,1,6,4])
# var=np.array([[1,5,2,6],[3,8,7,4]])
# # var = np.sort(var)
# var = np.sort(var,axis=0)
# print(var)

# FILTER
var = np.array([7,2,5,3,1,6,4])
f = [True,False,True,False,True,True,False]

new_a = var[f]
print(new_a)
print(type(new_a))
