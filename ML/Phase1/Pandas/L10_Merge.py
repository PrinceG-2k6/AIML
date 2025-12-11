import pandas as pd

var1 = pd.DataFrame({
    "A":[1,2,3,4],
    "B":[11,12,13,14]
})
var2 = pd.DataFrame({
    "A":[1,2,3,4],
    "C":[21,22,23,24]
})
var3 = pd.DataFrame({
    "A":[1,2,3,5],
    "C":[21,22,23,24]
})

# print(pd.merge(var1,var2,on="A"))

# # print(pd.merge(var1,var3,how="left"))
# # print(pd.merge(var1,var3,how="right"))
# print(pd.merge(var1,var3,how="outer",indicator=True))


var4 = pd.DataFrame({
    "A":[1,2,3,4],
    "C":[21,22,23,24]
})
var5 = pd.DataFrame({
    "A":[1,2,3,4],
    "C":[31,32,33,34]
})

# print(pd.merge(var4,var5,left_index=True,right_index=True,suffixes=("name","python")))


# CONCAT

sr1 = pd.Series([1,2,3,4])
sr2 = pd.Series([11,12,13,14])
var6 = pd.DataFrame({
    "A":[1,2,3,4],
    "C":[33,34]
})
print(pd.concat([sr1,sr2]))
print(pd.concat([var4,var5],axis=1,join="inner"))
# print(pd.concat([var1,var3],axis=1,join="inner"))