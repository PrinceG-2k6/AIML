import pandas as pd
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

"""

X_std = (X - Xmin)/(Xmax-Xmin)
X_scaled = X_std*(max-min) +min

"""

iris = load_iris()
x_train , x_test  ,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.2,random_state=42)
pipe_lr = Pipeline([('minmax',MinMaxScaler()),('lr',LogisticRegression())])
pipe_lr.fit(x_train,y_train)
score = pipe_lr.score(x_test,y_test)
print(score)
