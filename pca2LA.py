#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# # Q1. Eigenvalues and eigenvectors

# In[2]:


M=np.matrix([[11,-8,4],[-8,-1,-2],[4,-2,-4]])
M


# In[3]:


e1,e2=np.linalg.eig(M)
eval1=np.round(e1,4)
evec1=np.round(e2,4)
print(f"Eigenvalues of matrix M are:\n{eval1}")
print(f"\nEigenvectors of matrix M are:\n{evec1}")


# In[4]:


D=np.diag(eval1)
print(f"Diagonalised form:\n{D}")


# # Q2. SVD

# In[5]:


A=np.matrix([[1,0,1],[-1,1,0]])
A


# In[6]:


import scipy
U,S,V=scipy.linalg.svd(A)
print("SVD of matrix A=USV',where\n")
print(f"U=\n{np.round(U,1)}")
print(f"\n S=\n{np.round(S,1)}")
print(f"\n V=\n{np.round(V,1)}")


# # Q3.

# In[7]:


#3(a) loading the dataset

import pandas as pd
dt=pd.read_csv("train.csv")
dt


# In[8]:


#3(b) splitting dataset in 7:3 ratio for train-test analysis

from sklearn.model_selection import train_test_split 
y=dt['total_fare']
X=dt[['trip_duration','distance_traveled','num_of_passengers','fare','tip','miscellaneous_fees','surge_applied']]
X_train, X_test,y_train, y_test = train_test_split(X,y,
                                                   test_size=0.3,
                                                   random_state=100)


# In[9]:


#3(c) mlr model fitting and estimating predicted values

from sklearn.linear_model import LinearRegression 
model = LinearRegression()
model.fit(X_train,y_train)
predictions = model.predict(X_test)
print(f"Predicted values of Total fare are:\n{predictions}")


# In[10]:


from statsmodels.formula.api import ols
reg=ols('y~X',data=dt).fit()
reg.summary()


# R_square=1,
# adjusted R_square=1

# In[11]:


#3(d)
import math
from sklearn.metrics import mean_squared_error, r2_score
MSE=mean_squared_error(y_test, predictions)
RMSE=math.sqrt(MSE)
print(f"RMSE={RMSE}")


# In[12]:


from statsmodels.stats.outliers_influence import variance_inflation_factor 
vif_data = pd.DataFrame() 
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) 
                          for i in range(len(X.columns))]
print(vif_data)


# In[13]:


#since almost all VIF values of the independent variables are less than 5,
#we can conclude there is no such multicollinearity present in the dataset.

