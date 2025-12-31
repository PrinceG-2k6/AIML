import sklearn
from sklearn import datasets
from sklearn.datasets import fetch_openml 
import pandas as pd

"""
4 steps to build a machine learning model
DATA PREPARATAION
    |
    |
FEATURE ENGINEERING
    |
    |
DATA MODELING
    |   
    |
PERFORMANCE MEASURE 


DATA + ALGORITHM = MODEL
"""
total_data  = pd.read_csv("./ML/Phase2/Seed_Data.csv")
# print(total_data.describe)

x = total_data.iloc[:,0:7]
# print(x.info)

y = total_data.iloc[:,7]
# print(y.info)

from sklearn import svm
from sklearn.svm import SVC

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=13)

from sklearn.preprocessing import StandardScaler

sc= StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

clf= svm.SVC()
clf.fit(x_train,y_train)

pred_clif=clf.predict(x_test)
print(sklearn.metrics.accuracy_score(y_test,pred_clif))
print(sklearn.metrics.classification_report(y_test,pred_clif))