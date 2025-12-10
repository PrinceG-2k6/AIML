import pandas as pd 

# # x= pd.Series([1,2,3,4])
# x= pd.Series([1,2,3,4],index=['a','s','d','f'],dtype="float",name="python")
# print(x)
# print(type(x))
# # print(x[2])

# dic = {
#     "name":['python','c','c++','java'],
#     'por':[12,13,14,15],
#     "rank":[1,2,3,4]
# }
# var = pd.Series(dic)
# print(var)

# Series are used because it can perform operation without broadcassting

s1 =pd.Series(12,index=[1,2,3,4,5])
s2 =pd.Series(12,index=[1,2,3,4,5,6,7,8])

print(s1)
print()
print(s1)
print()
print(s1+s2)