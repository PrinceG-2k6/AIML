import  numpy as np
# ARRAY

x = np.array({1,2,3,4,5});
print(x)
print(type(x))
# l=[]
# for i in range(1,6):
#     int_l = int(input("Enter : "))
#     l.append(int_l)

# print(np.array(l))


# ar2 = np.array([[1,2,3,4],[5,6,7,8]])
# print(ar2.ndim)

# ar3 = np.array([[[1,2,3,4]]])
# print(ar3.ndim)

ar10 = np.array([1,2,3,4],ndmin=10)
print(ar10.ndim)