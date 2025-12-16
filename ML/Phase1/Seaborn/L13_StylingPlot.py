import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

var = sns.load_dataset("tips")

m={
    "Male":"o",
    "Female":"<"
}
# plt.figure(figsize=(3,12))
sns.set(style="whitegrid")
sns.barplot(x=var["day"],y=var["total_bill"])

sns.set_context("poster",font_scale=2)
sns.despine()
plt.show()