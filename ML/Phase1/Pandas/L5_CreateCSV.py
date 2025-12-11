import pandas as pd 

dis={
    "a":[1,2,3,4,5,6],
    "s":[2,3,4,5,6,None],
    "d":[3,4,5,6,None,None]

}
d = pd.DataFrame(dis)

print(d)
d.to_csv("./ML/Phase1/Pandas/L5_CreateCSV.csv")
d.to_csv("./ML/Phase1/Pandas/L5_CreateCSV1.csv",index=False)
d.to_csv("./ML/Phase1/Pandas/L5_CreateCSV2.csv",index=False,header=["x","y","z"]) 