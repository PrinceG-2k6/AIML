import pandas as pd

var1 = pd.DataFrame({
    "A":[1,2,3,4],
    "B":[11,12,13,14]
},index=["a","b",'c',"d"])
var2 = pd.DataFrame({
    "C":[10,20],
    "D":[21,22]
},index=["a","b"])
var3 = pd.DataFrame({
    "C":[10,20],
    "B":[21,22]
},index=["a","b"])
# Both must have same index

# print(var1.join(var2))
# print(var2.join(var1))
# print(var2.join(var1,how="outer"))

# print(var3.join(var1,how="outer",lsuffix="_10_",rsuffix="-0-"))


# print(var3.append(var3))