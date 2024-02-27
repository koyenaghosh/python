#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as p
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


d=np.random.normal(4,2.5,50)
d


# In[3]:


T_st=[]
for i in range(1,20001):
    d1=np.random.normal(4,2.5,50)
    #data.append(d1)
    T=(np.sqrt(50)*(d1.mean()-4))/2.5
    T_st.append(T)
print(T_st)


# In[4]:


plt.hist(T_st)
plt.show()


# In[21]:


np.quantile(d,0.95)


# In[ ]:




