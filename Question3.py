# Q3. How do you interpret the slope and intercept in a linear regression model? Provide an example using
# a real-world scenario.

# Answer - 

# In SLR , The relationship is modeled as a straight line, represented by the equation: Y = aX + b, where Y is the dependent variable, 
# X is the independent variable, a is the slope, and b is the intercept.

# we can simply calculate this python code - 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('height-weight.csv')
print(df.head())

X = df[['Weight']] ## independent feature
Y = df['Height'] ## dependent feature

from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.20,random_state=42)

print(X_train.shape,X_test.shape)
print(Y_train.shape,Y_test.shape)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test) 

plt.scatter(X_train,Y_train)

## Model Training 

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

## Training the train data 
regressor.fit(X_train,Y_train)

print(regressor.intercept_)
print(regressor.coef_)
# from this we can calculate intercept and slope