import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import pickle

data=pd.read_csv("diabetes.csv")
x=data.drop("Outcome",axis=1)
y=data['Outcome']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=20)

from sklearn.linear_model import LinearRegression
le=LinearRegression()
le.fit(x_train,y_train)
y_pred=le.predict(x_test)

pickle.dump(le,open('extra.pkl','wb'))

