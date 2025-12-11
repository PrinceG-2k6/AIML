import pandas as pd 

csv_1= pd.read_csv("./ML/Phase1/Pandas/L5_CreateCSV2.csv")
print(csv_1)
print() 

# print(csv_1.dropna())

# print(csv_1.dropna(axis=1))

# print(csv_1.dropna(how="any"))
# print(csv_1.dropna(how="all"))

# print(csv_1.dropna(subset=["y"]))

# print(csv_1.dropna(inplace=True))


# print(csv_1.dropna(thresh=2))


print(csv_1.fillna("Python",limit=1))

# print(csv_1.fillna({"y":"Python","z":"Pyth"}))


# print(csv_1.fillna(method="ffill"))
# print(csv_1.fillna(method="ffill",axis=1))

# csv_1.fillna(12,inplace=True)
# print(csv_1)