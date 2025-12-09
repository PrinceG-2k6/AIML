import numpy as np

var = np.array([1,2,3,4,5])

co =var.copy()
print(var)
print(co)#SHallow Copy

# var[0] = 10
# co[0]=12
# print(var)
# print(co)

vi = var.view()
vi[0]=10
print(var)#Deep Copy
var[0]=100
print(vi)