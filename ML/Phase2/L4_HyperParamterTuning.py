import pandas as pd
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
# A final decision  is concluded as max voting
"""
Group of people decided to go on a trip
cities to be selected was  Mumbai,Chennai,Kolkata 
Max Friend Selected Kolata
Hence Trip planned at Kolkata

this is a ***RANDOM FOREST CLASSIFIER***
"""


iris = load_iris()
x_train , x_test  ,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.2,random_state=30)

clf= RandomForestClassifier(n_estimators=2,min_samples_split=3,min_samples_leaf=2)  
clf.fit(x_train,y_train)
pred_clf = clf.predict(x_test)


print(sklearn.metrics.accuracy_score(y_test,pred_clf))


from sklearn.model_selection import GridSearchCV
param_grid ={'n_estimators':[2,5,10,20],'min_samples_split':[2,3],'min_samples_leaf':[1,2,3]}
grid_search =GridSearchCV(estimator=clf,param_grid=param_grid)
grid_search.fit(x_train,y_train)

# print(grid_search.best_params_)

clf= RandomForestClassifier(n_estimators=5,min_samples_split=2,min_samples_leaf=1)  
clf.fit(x_train,y_train)
pred_clf = clf.predict(x_test)
print(sklearn.metrics.accuracy_score(y_test,pred_clf))