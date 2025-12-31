import sklearn
from sklearn import datasets


#LOADING INBUILD DATASETS 

# print(dir(datasets)) # All Dataset  Names

# iris =datasets.load_iris()
# # print(iris.feature_names) # All Column Names
# # print(iris.data)# All Row Names
# # print(iris.target)
# # print(iris.target_names)
# print(iris.DESCR)


# FETCHING DATASETS FROM openml.org

from sklearn.datasets import fetch_openml 
mice = fetch_openml(name="miceprotein",version=4)
print(mice.details)

