import pandas as pd

var = pd.DataFrame({
    "A":[1,2,3,4],
    "B":[5,6,7,8]
})

var.insert(1,"Python",var["A"])
# (index,coulmn_name,Data)
var.insert(0,"Start",["a","b","c","d"])

var["slice"] = var["A"][1:3]
print(var)
print()

var1 = var.pop("B")
print(var1)
print()
del var["slice"]
print(var)

