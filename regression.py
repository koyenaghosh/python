#!/usr/bin/env python
# coding: utf-8

# **Lab work:  Date: 07.11.2023**
# 
# **download a dataset from Kaggle with atleast more than 10 attributes, find correlation coefficients among the attributes,
# next using feature selection methods try to select the features for regression analysis. Feature selection method: 1. Mutual information score, 2. Forward selection method, 3. Backward selection method,also test multicollinearity among the variables,  after train- test splitting try  regression analysis,Find the loss function/ error term.**

# In[3]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


data=pd.read_csv("Student_Performance.csv")


# In[5]:


data['Extracurricular Activities']=data['Extracurricular Activities'].replace({'Yes':1,'No':0})


# # Data Source
# https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression
# 
# 
# 
# 

# # Data Description
# Description:
# The Student Performance Dataset is designed to examine the factors influencing academic student performance. The dataset consists of 10,000 student records, with each record containing information about various predictors and a performance index.
# 
# Independent Variables or Covariates:
# 
# Hours Studied: The total number of hours spent studying by each student.
# 
# Previous Scores: The scores obtained by students in previous tests.
# 
# Extracurricular Activities: Whether the student participates in extracurricular activities (Yes or No).
# 
# Sleep Hours: The average number of hours of sleep the student had per day.
# Sample Question Papers Practiced: The number of sample question papers the student practiced
# 
# (Target Variable)Performance Index: A measure of the overall performance of each student. The performance index represents the student's academic performance and has been rounded to the nearest integer. The index ranges from 10 to 100, with higher values indicating better performance.
# 
# The dataset aims to provide insights into the relationship between the predictor variables and the performance index. Researchers and data analysts can use this dataset to explore the impact of studying hours, previous scores, extracurricular activities, sleep hours, and sample question papers on student performance.

# In[6]:


data


# In[7]:


X=data[['Hours Studied','Previous Scores',
        'Extracurricular Activities','Sleep Hours',
        'Sample Question Papers Practiced']]
y=data['Performance Index']


# In[8]:


data.corr()


# # Correlation Heatmap

# In[9]:


dataplot = sns.heatmap(data.corr(),cmap="YlGnBu", annot=True)
plt.show()


# In a correlation heatmap, the correlation between each variable can be represented using 
# a color scale where lighter colors indicate negative correlations and darker colors 
# represent positive correlations. Here, the correlation between performance index and
# previous scores is 0.92 with a dark blue shade indicating strong positive correlation. 
# Similarly the light yellow shades represent negative correlations whereas the lighgt
# blue shades denote moderately positive correlations

# # Scatter plot

# In[10]:


d=data.head(100)
x1=d['Hours Studied']
x2=d['Previous Scores']
x3=d['Extracurricular Activities']
x4=d['Sleep Hours']
x5=d['Sample Question Papers Practiced']
Y=d['Performance Index']
plt.figure(figsize=(5,3.2))
plt.title("SCATTER PLOT")
plt.xlabel("Covariates")
plt.ylabel("Performance Index")
plt.scatter(x1,Y,label='x1 vs y',s=10)
plt.scatter(x2,Y,label='x2 vs y',s=10)
plt.scatter(x3,Y,label='x3 vs y',s=10)
plt.scatter(x4,Y,label='x4 vs y',s=10)
plt.scatter(x5,Y,label='x5 vs y',s=10)
plt.legend()
plt.show()


# Here we have constructed a multiple-scatter plot each for covariates vs target variable. the x2 vs y plot (Previous scores vs performance index) shows a linear curve with an increasing trend.
# 
# The other curves are st. lines parallel to the y-axis. This scenario typically occurs when there is little to no variability in one of the variables, resulting in a straight vertical line.

# # Train-test analysis

# In[11]:


from sklearn.model_selection import train_test_split 
X_train, X_test,y_train, y_test = train_test_split(X, y,
                                                   test_size=0.3,
                                                   random_state=100) 


# A dataset is splitted into two subsets- training and testing sets. the splitting is done following 70:30 ratio. The training set is used to train the model and the test set is used to evaluate the model's performance over the unseen data i.e., prediction on the dataset.

# In[12]:


from sklearn.linear_model import LinearRegression 
model = LinearRegression() 
model.fit(X_train,y_train)
predictions = model.predict(X_test)
print(f'Predicted values of performance index are:\n{predictions}')


# # Model fitting and analysis

# In[13]:


from statsmodels.formula.api import ols
reg=ols('y~X',data=data).fit()
reg.summary()


# - **R-squared:** =0.989 indicates the proportion of the variance in the dependent variable (y) that can be explained by the independent variables in the model. A value close to 1 suggests a very good fit.
# - **F-statistic:** 1.757* 10^5
#   -The F-statistic tests the overall significance of the model. A high F-statistic value, along with a low associated p-value, suggests that the model is statistically significant.
# 
#     If Y=a+ b1* x1 + b2* x2 + b3* x3 + b4* x4 + b5* x5 is the regression equation,
# - **Intercept** a=-34.0756
# - **Coefficients for Independent Variables (X1, X2, X3, X4, X5):**
#      -b1: 2.8530
#      -b2: 1.0184
#      -b3: 0.6129
#      -b4: 0.4806
#      -b5: 0.1938
#      
# - The "t" column provides the t-statistic for each coefficient, and the "P>|t|" column provides the associated p-value.
# - If the p-value is less than the significance level (commonly 0.05), the coefficient is considered statistically significant.
# - here, all coefficients have very low p-values (0.000), indicating that they are statistically significant.
# 
# - **Omnibus Test:** Indicates the normality of residuals. P-value (0.146) suggests presence of normality.
# 
# - **Durbin-Watson Statistic (2.001):** Suggests little evidence of significant autocorrelation (residual independence).
# 
# - **Jarque-Bera Test:** Tests skewness and kurtosis. P-value (0.133) indicates no significant deviation from a normal distribution.
# 
# - **Skewness (0.013):** symmetric distribution
# 
# - **Kurtosis (3.095):** Close to normal (mesokurtic).
# 
# - **Condition Number (452):** Indicates multicollinearity.

# # Loss function

# In[14]:


from sklearn.metrics import mean_squared_error, mean_absolute_error 
print('mean_squared_error : ', mean_squared_error(y_test, predictions)) 
print('mean_absolute_error : ', mean_absolute_error(y_test, predictions)) 


# lower values of MSE and MAE denotes greater precision of the model.

# # Forward feature selection

# In[15]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from mlxtend.feature_selection import SequentialFeatureSelector
sfs = SequentialFeatureSelector(
    RandomForestClassifier(n_jobs=1),
    k_features=(1,5),
    forward=True,
    verbose=2,
    scoring='accuracy',
    cv=None).fit(X_train,y_train)


# In[16]:


sfs.k_feature_idx_


# In[17]:


sfs.k_feature_names_


# In[18]:


sfs.k_score_


# In[19]:


pd.DataFrame.from_dict(sfs.get_metric_dict()).T


# # Backward elimination

# In[29]:


sfsb = SequentialFeatureSelector(
    RandomForestClassifier(n_jobs=1),
    k_features=(1,5),
    forward=False,
    verbose=2,
    scoring='accuracy',
    cv=None).fit(X_train,y_train)


# In[21]:


sfsb.k_feature_idx_


# In[22]:


sfsb.k_feature_names_


# In[23]:


sfsb.k_score_


# In[24]:


pd.DataFrame.from_dict(sfsb.get_metric_dict()).T


# # Mutual Information Score

# In[25]:


from sklearn.feature_selection import mutual_info_regression
mi_scores = mutual_info_regression(X, y)


# In[26]:


feature_scores = pd.Series(mi_scores, index=X.columns, 
                           name='Mutual Information Score')
print(feature_scores.sort_values(ascending=False))


# # Multicollinearity test(VIF)

# In[28]:


from statsmodels.stats.outliers_influence import variance_inflation_factor 
vif_data = pd.DataFrame() 
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) 
                          for i in range(len(X.columns))]
print(vif_data)


# The VIF analysis indicates varying levels of multicollinearity among the covariates, with "Previous Scores" and "Sleep Hours" exhibiting high multicollinearity (near about 10).
