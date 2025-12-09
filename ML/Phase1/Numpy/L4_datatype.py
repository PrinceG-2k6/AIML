import numpy as np

# bool_ True False
# int_ Default(in C, long)
# intc (in C ,int)
# int8 (-128 to 127)
# int16 
# int32
# int64
# uint8 unsigned 0 - 255
# uint 16 ,32,64
# same float 

# # var = np.array([1,2,3,4])

# # var = np.array([1,2,3,4.1])

# # var = np.array([True,False])



# print("Data Type ", var.dtype)

x =np.array([1,2,3,4],dtype=np.int8)

# x =np.array([1,2,3,4],dtype="bool")
# x =np.array([1,2,3,4],dtype="f")

# new = np.float32(x)
# print("Data Type ", x.dtype)
# print(x)

# print("Data Type ", new.dtype)
# print(new)

y = x.astype(float)
print("Data Type ", y.dtype)
print(y)