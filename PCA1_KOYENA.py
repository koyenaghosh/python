#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


# In[42]:


A=np.matrix([[1,-2,-4],[2,0,-3],[3,-7,1]])


# In[43]:


B=np.matrix([[-1,2,-4],[2,5,-3],[3,-7,7]])


# In[44]:


print(np.dot(A,B))


# In[45]:


print(np.dot(B,A))


# In[46]:


print(np.subtract(A,B))


# In[47]:


print(np.subtract(B,A))


# In[48]:


AB=np.dot(A,B)
print(AB)


# In[49]:


print(np.trace(AB))


# In[63]:


m=np.matrix([[1,2,-1],[2,-1,1],[-1,2,3]])
n=np.matrix([[1],[3],[7]])
print("values of x1,x2,x3 are\n",np.linalg.solve(m,n))


# In[60]:


e1,e2=np.linalg.eig(m)
print("eigenvalues of the coefficient matrix are:\n",e1)


# In[59]:


print("rank of the coefficient matrix is",np.linalg.matrix_rank(m))


# In[76]:


data=pd.read_csv("air.csv")


# In[77]:


print(data)


# In[78]:


d1=data.head(100)


# In[79]:


x=d1['state_name']
y=d1['aqi']
plt.scatter(x,y, c='black')
plt.title("scatter plot")
plt.xlabel("name of the states")
plt.ylabel("aqi")
plt.xticks(rotation=90)
plt.colorbar()
plt.show()


# In[80]:


plt.title("histogram")
plt.xlabel("aqi")
plt.ylabel("frequency")
plt.hist(y)
plt.show()


# In[84]:


plt.bar(x,y)
plt.title("bar diagram")
plt.xlabel("name of the states")
plt.ylabel("aqi")
plt.xticks(rotation=90)
plt.show()


# In[85]:


plt.plot(y)
plt.title("line diagram")
plt.xlabel("aqi")
plt.ylabel("frequency")
plt.xticks(rotation=90)
plt.show()


# In[89]:


d2=d1.drop_duplicates(['aqi'])


# In[96]:


d3=d2.head(5)


# In[97]:


print(d3)


# In[101]:


a=d3['aqi']
plt.pie(a)
plt.title("pie chart")
plt.show()


# In[ ]:




