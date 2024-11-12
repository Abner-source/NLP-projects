#importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection  import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
#reading the dataset
df=pd.read_csv('lois_continuous.csv', low_memory=False)
df['Temperature water continuous']=pd.to_numeric(df['Temperature water continuous'], errors='coerce')
#print(df.head())
df_cleaned=df.dropna()
X=df_cleaned[['Temperature water continuous']]
y=df_cleaned['Oxygen dissolved continuous']
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2, random_state=42)
#creating and training linear regression test
model=LinearRegression()
model.fit(X_train, y_train)
#make prediction on training data
y_pred=model.predict(X_test)
#evaluating the model
mse=mean_squared_error(y_test, y_pred)
rms=r2_score(y_test, y_pred)
print('mean squared error=',mse)
print('r2 score=',rms)


