import pandas as pd 
import numpy as np 

csv_1= pd.read_csv("./ML/Phase1/Pandas/L5_CreateCSV2.csv")
print(csv_1)
print() 

# print(csv_1.index)
# print(csv_1.columns)
# # print(csv_1.describe())

# print(csv_1.head(2))
# print(csv_1.tail(2))
# print(csv_1[1:4])

# print(csv_1.index.array)

# print(csv_1.to_numpy())


# print(np.array(csv_1))

# print(csv_1.sort_index(axis=0,ascending=False))

# csv_1.loc[0,"x"]=100

# print(csv_1.loc[[2,3],["x","y"]])

# print(csv_1.iloc[1,1])


print(csv_1.drop("z",axis=1))
print(csv_1)