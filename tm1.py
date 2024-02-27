#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np
import statistics as stat


# In[44]:


x=[1,5,7,8,9]
z=np.array(x).tolist()


# In[45]:


print(z)


# In[46]:


y=[2,4,3,9,8]
w=np.array(y).tolist()
print(w)


# In[47]:


type(w)


# In[48]:


z+w #addition of two arrays


# In[49]:


w-z #subtraction of two arrays


# In[50]:


z**2 #squaring the array 'z'


# In[51]:


stat.mean(w)


# In[52]:


stat.stdev(w)


# In[ ]:




