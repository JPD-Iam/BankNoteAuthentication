from sklearn.ensemble import RandomForestClassifier
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

data=pd.read_csv("/Users/jyotiprakashdey/Downloads/BankNote_Authentication.csv")
data.head()
X=data.iloc[:,:-1]
Y=data.iloc[:,-1]
Y.head()
X.head()
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=0)
classifier=RandomForestClassifier()
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)
score=accuracy_score(y_test,y_pred)

pickle_out=open("classifier.pkl","wb")
pickle.dump(classifier,pickle_out)
pickle_out.close()
classifier.predict([[2,3,4,1]])