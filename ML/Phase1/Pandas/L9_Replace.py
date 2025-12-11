import pandas as pd 

csv_1= pd.read_csv("./ML/Phase1/Pandas/L5_CreateCSV2.csv")
print(csv_1)
print() 

# print(csv_1.replace(to_replace=3,value="rep"))
# print() 
# print(csv_1.replace([1,2,3],"rep"))
# print() 


# print(csv_1.replace(["A-Aa-z"],"rep2",regex=True))
# print() 

# print(csv_1.replace(1,method="bfill",limit=1))

# INTERPOLATE

print(csv_1.interpolate(method="linear",axis=1,limit=1,limit_direction="forward"))
