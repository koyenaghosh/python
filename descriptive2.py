#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np   #for mathematical purposes
import pandas as pd  #used for working with datasets and data-handling
import os            #os, matplotlib.pyplot and seaborn are packages used for data visualisation purposes.
import matplotlib.pyplot as mp
import seaborn as sb


# In[3]:


data=pd.read_csv("heartdata.csv") #read .csv file as a data frame.


# In[4]:


data 


# In[5]:


data.shape  #showing the number of rows and columns of the dataset.


# In[6]:


d=data.drop(['age.1'],axis=1) #dropping "age.1" column that represents age in days.


# In[7]:


d


# In[8]:


d1=d.head(10) #shows first 10 rows of the data frame


# In[9]:


d.tail(10) #shows first 10 columns of the data frame


# In[10]:


d.isnull().sum().sum() #computes number of missing values present in the dataset.


# In[11]:


d1.index=['row 1','row 2','row 3','row 4','row 5','row 6','row 7','row 8','row 9','row 10'] #indexing row names


# In[12]:


d.info() #printing necessary informations about the dataset.


# In[13]:


d.describe() #summarising values of all descriptive statistical measures like mean,sd,percentiles etc.


# In[14]:


d['height'].mean() #printing mean of a particular column.


# In[15]:


d.mean() #printing mean of the entire dataset.


# In[16]:


d.std() #printing standard deviation of the dataset.


# In[17]:


d.corr() #prints the correlation matrix of the dataset.


# In[18]:


d.median() #prints median of the entire dataset.


# In[19]:


d.mode() #prints mode of the dataset.


# In[20]:


d.drop_duplicates(subset=['age']) #dropping duplicate values from the column 'age'.


# In[21]:


d.loc[(d['age']<60)&(d['height']>185)] #printing age <60 and height>185 cm.


# In[22]:


x1=d['height']


# In[23]:


y1=d['weight']


# In[24]:


x1


# In[25]:


y1


# # SCATTER PLOT

# In[26]:


mp.figure(figsize=(5,3.5))
mp.scatter(x1,y1,s=20, c='red', marker='o', alpha=0.8)
mp.title("scatter plot")
mp.xlabel("HEIGHT")
mp.ylabel("WEIGHT")
mp.xticks(rotation=90)
mp.colorbar()
mp.show()


# In[27]:


#The scatter plot is constructed with the heights of the patients along the X-axis and their corresponding weights
#along the Y-axis. Most of the patients have heights between 150-180 cms , as observed from the plot.
#Also, the two variables Height and Weight are more or less positively correlated.


# # BOX PLOT

# In[28]:


mp.figure(figsize=(5,3.5))
mp.title("box plot")
mp.boxplot(d1['bp_lo'])
mp.show()


# In[29]:


#The above box plot for low blood pressures shows the maximum value at 100, minimum value at 60, 
#first quartile (Q1=78),second quartile or median (Q2=80) and 
#the third quartile (Q3=90). Clearly the data is positively skewed with no visible outliers.


# # LINE DIAGRAM

# In[30]:


mp.title("Line diagram")
mp.xlabel("blood_pressure_hi")
mp.ylabel("no. of persons")
a=d1['bp_hi']
mp.plot(a)
mp.show()


# In[31]:


#The line diagram shows the systolic pressure (bp_hi) along the X-axis and the 
#corresponding number of persons along the Y-axis. 
#Maximum number of patients  i.e 180, have a systolic blood pressure of around 60 mm of Hg.


# # BAR DIAGRAM

# In[54]:


mp.title("Bar diagram")
sb.barplot(x='age',y='cholesterol',data=d1)
mp.show()

