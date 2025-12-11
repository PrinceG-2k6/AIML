import pandas as pd 

# var = pd.DataFrame({
#     "days":[1,2,3,4,5,6],
#     "eng":[10,13,14,16,23,16],
#     "maths":[19,12,16,18,20,12]
# })

# print(var)
# print(pd.melt(var,id_vars="eng",var_name="pyhton",value_name="wst"))


print("\n================= BASIC DATAFRAME =================")
var = pd.DataFrame({
    "days": [1,2,3,4,5,6],
    "st_name": ["a","b","c","a","b","c"],
    "eng": [10,12,14,15,16,12],
    "maths": [17,18,19,13,14,16]
})
print(var)

# ---------------------------------------------------
print("\n================= PIVOT (FULL TABLE) =================")
pivot_full = var.pivot(index="days", columns="st_name")
print(pivot_full)

# ---------------------------------------------------
print("\n================= PIVOT (ONLY ENG VALUES) =================")
pivot_eng = var.pivot(index="days", columns="st_name", values="eng")
print(pivot_eng)

# ---------------------------------------------------
print("\n================= DUPLICATE DATAFRAME =================")
var2 = pd.DataFrame({
    "days": [1,1,1,1,1,2,2],
    "st_name": ["a","b","a","a","b","a","b"],
    "eng": [10,12,14,15,16,14,12],
    "maths": [17,18,19,13,14,16,15]
})
print(var2)

# ---------------------------------------------------
print("\n================= PIVOT_TABLE (MEAN) =================")
pt_mean = var2.pivot_table(index="st_name", columns="days", aggfunc="mean")
print(pt_mean)

# ---------------------------------------------------
print("\n================= PIVOT_TABLE WITH VALUES =================")
pt_vals = var2.pivot_table(index="st_name", columns="days", values="eng", aggfunc="mean")
print(pt_vals)

# ---------------------------------------------------
print("\n================= PIVOT_TABLE WITH MARGINS (TOTAL) =================")
pt_margins = var2.pivot_table(
    index="st_name",
    columns="days",
    aggfunc="mean",
    margins=True
)
print(pt_margins)
