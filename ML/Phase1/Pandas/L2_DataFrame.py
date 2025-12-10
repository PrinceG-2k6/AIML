import pandas as pd 

# x= pd.DataFrame([1,2,3,4])
# print(x)
data = {
    "a":[1,2,3,4,5],
    "b":[1,4,9,16,25],
    "c":[1,8,27,64,125]
}
# var = pd.DataFrame(data)
var = pd.DataFrame(data,columns=["a","b"],index=[9,8,7,6,5])
print(var)
print(var["a"][5])

x= pd.DataFrame([[1,2,3,4],[5,6,7,8]])
print(x)
data = {
    "a":pd.Series([1,2,3,4,5]),
    "b":pd.Series([1,4,9,16,25])
}
sr =pd.DataFrame(data)

print(data)