import numpy as np

x =[1,2,3,4,5,6,7]
# for i in x:
#     print(i)
# var = np.array(x)
# for i in var:
#     print(i)

var = np.array([[1,2,3,4],[5,6,7,8]])
# for i in var:
#     print(i)

# for i in var:
#     for j in i:
#         print(j)

# for i in np.nditer(var,flags=['buffered'],op_dtypes=["S"]):
for i in np.nditer(var):
    print(i)

for i,d in np.ndenumerate(var):
    print(i,d)