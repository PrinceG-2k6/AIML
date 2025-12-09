import numpy as np

var1 = np.array([1,2,3])#1x3

var2 = np.array([[1],[2],[3],[4]])#4x1

# print(var1+var2) #Cant possible ,Broadcasting required
# for addition we need same dimension
#  after broadcasting we can add 2 different dimensionn matrix if:
# 1) dimension same 
# 2) one of value of dimension shold same

print(var1)
print(var1.shape)
print()

print(var2)
print(var2.shape)
print()

print(var1+var2)#BroadCasting Done

# broadcating of 2x1 and 2x3 result in 2x3
# because
# first comparing 1 and 3 ===> 3 max

# Then comparing 2 and 2 ===> 2 max
# hence 2x3