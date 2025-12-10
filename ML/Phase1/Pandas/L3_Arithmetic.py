import pandas as pd 

var = pd.DataFrame({
    "A":[1,2,3,4],
    "B":[5,6,7,8]
})

var["Sum"]=var["A"]+var["B"]
var["Subtract"]=var["A"]-var["B"]
var["Product"]=var["A"]*var["B"]
var["Divide"]=var["A"]/var["B"]
# print(var)

var["Check"]=var["A"]<=3
print(var)