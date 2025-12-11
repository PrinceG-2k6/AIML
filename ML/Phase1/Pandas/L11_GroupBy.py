import pandas as pd 

var = pd.DataFrame({
    "name":["a","b","c","a","a","b","c","c"],
    "S_1":[11,12,1,12,12,12,14,1,],
    "S_2":[21,22,23,24,23,21,22,24]
})
print(var)

var_1 = var.groupby("name")
# print(var_1)

# for x,y in var_1:
#     print()
#     print(x)
#     print(y)

var_2=var_1.get_group("a")
# print(var_2)

print(var_1.min())
print(var_1.max())