import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
df=pd.read_csv('processed_cleveland.csv')
df_cleaned=df.dropna()
#print(df.head())
x=df_cleaned.drop(columns=['num'])
y=df_cleaned['num']
x=pd.get_dummies(x, drop_first=True)
x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.2, random_state=42)
#creating logistic regression model
model=LogisticRegression(max_iter=1000)
#fit the model
try:
    model.fit(x_train,y_train)
except Exception as e:
    print("Error during fitting model:{e}")
#predict on test data
y_pred=model.predict(x_test)
#calculating accuracy
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy:",accuracy)
#getting the feature importance
importance=model.coef_[0]
#printing feature importance
print("\nFeature Importance")
for i, feature_name in enumerate(x.columns):
    print(f'Feature:{feature_name}, Importance:{importance[i]:.4f}')
#print(x_train.shape)
#print(y_train.shape)
#print(x.dtypes)