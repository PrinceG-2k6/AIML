import numpy as np

# var1 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])

# var2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

# print(var1)
# print(var2)

# Multiplication vary in both 


var1 = np.matrix([[1,2],
                  [3,4]])
var2 = np.matrix([[5,6],
                  [7,8]])

# var3 = np.multiply(var1,var2)
# print(var3)
# print(var1.dot(var2))
print(var1)
# print(np.transpose(var1))
# print(var1.T)

# print(np.swapaxes(var1,0,1))

# print(np.linalg.inv(var1))

# print(np.power(var1,2))
# print(np.linalg.matrix_power(var1,2))

print(np.linalg.det(var1))


