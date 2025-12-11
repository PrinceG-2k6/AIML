import pandas as pd

csv_1= pd.read_csv("./ML/Phase1/Pandas/L5_CreateCSV2.csv")
print(csv_1)
print()
# csv_1= pd.read_csv("./ML/Phase1/Pandas/L5_CreateCSV2.csv",nrows=3)
# print(csv_1)
# print()
# csv_1= pd.read_csv("./ML/Phase1/Pandas/L5_CreateCSV2.csv",usecols=["x","y"])
# print(csv_1)
# print()

# csv_1= pd.read_csv("./ML/Phase1/Pandas/L5_CreateCSV2.csv",skiprows=[0])
# print(csv_1)
# print()

# csv_1= pd.read_csv("./ML/Phase1/Pandas/L5_CreateCSV2.csv",index_col="x")
# print(csv_1) 
# print()


# csv_1= pd.read_csv("./ML/Phase1/Pandas/L5_CreateCSV2.csv",header=1)
# print(csv_1)
# print() 

# csv_1= pd.read_csv("./ML/Phase1/Pandas/L5_CreateCSV2.csv",names=["col1","col2","col3"])
# print(csv_1)
# print() 

# OR

# csv_1= pd.read_csv("./ML/Phase1/Pandas/L5_CreateCSV2.csv",header=None,prefix="col")
# print(csv_1)
# print() 

csv_1= pd.read_csv("./ML/Phase1/Pandas/L5_CreateCSV2.csv",dtype={"x":"float","y":"string"})
print(csv_1)
print() 