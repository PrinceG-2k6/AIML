import numpy as np

"""
Shuffle
Unique
Resizee
Flatten
Ravel
"""

var = np.array([1,2,3,4,3,2,4,1])
# np.random.shuffle(var)

# x = np.unique(var,return_index=True,return_counts=True)

var2 = np.resize(var,(3,2))



print(var)
# print(x)
print(var2)
# print(var2.flatten(order="F"))

# print(var2.flatten(order="C"))
# print(var2.flatten(order="A"))
# print(var2.flatten(order="K"))

print("Ravel : ",np.ravel(var2))