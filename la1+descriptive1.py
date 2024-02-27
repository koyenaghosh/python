#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import os
import matplotlib.pyplot as mp
import seaborn as sb


# In[3]:


mat1=np.matrix([[1,2,3],[2,3,4],[3,4,5]])
print(mat1)


# In[4]:


mat2=np.matrix([[1,8,3],[0,2,4],[1,9,15]])


# In[5]:


print(mat2)


# In[6]:


print(mat1+mat2)


# In[7]:


print(np.dot(mat1,mat2))


# In[8]:


e1,e2=np.linalg.eig(mat1)
print("eigenvalues:\n",e1)
print("eigenvectors:\n",e2)


# In[9]:


v1=np.array([-0.38508979,-0.82767094,0.40824829])


# In[10]:


print(v1)


# In[11]:


v2=np.array([-0.55951021, -0.14241368, -0.81649658])


# In[12]:


print(v2)


# In[13]:


print(np.dot(v1,v2))


# In[14]:


v3=np.array([-0.73393063,  0.54284358,  0.40824829])


# In[15]:


print(np.dot(v1,v3))


# # solve:2x-y+3z=5
# #           x+7y=2
# #           y+6z=9

# In[16]:


mat3=np.matrix([[2,-1,3],[1,7,0],[0,1,6]])
mat4=np.matrix([[5],[2],[9]])
print(np.linalg.solve(mat3,mat4))
print("\n")
print(np.linalg.inv(mat3))


# # tabulating a given dataset using dictionary

# In[17]:


dict1={'Names':['Rimi','Simi','Mimi'],'Blood groups':['A+','O+','AB-'],'Home Town':['Kolkata','Kalyani','Kanpur']}


# In[18]:


T=pd.DataFrame(dict1)


# In[19]:


T.index=[1,2,3]


# In[20]:


T


# In[21]:


T.T


# # Data Handling

# In[27]:


df=pd.read_csv("koyena.csv")


# In[25]:


os.chdir("C:\\Users\\KOYENA GHOSH\\Downloads")


# In[26]:


os.getcwd()


# In[28]:


df


# In[29]:


df.shape


# In[30]:


df1=df.drop(['Unnamed: 14','Unnamed: 15'],axis=1)


# In[284]:


df1


# In[31]:


df2=df1.head(5)
df2


# In[32]:


print(df1.tail(5))


# In[33]:


print(df1['oldpeak'][298])


# In[34]:


df2.index=['A','B','C','D','E']


# In[35]:


df2


# In[36]:


df1.describe()


# In[37]:


df1.info()


# In[38]:


df1


# In[39]:


df3=df1.loc[(df1['cp']<3)&(df1['thalach']>155)]


# In[40]:


df3


# In[41]:


df1.mean()


# In[42]:


df1.median()


# In[43]:


df1.std()


# In[44]:


df1.corr()


# In[45]:


df4=df1.drop_duplicates(subset=['restecg'])


# In[46]:


df4


# In[47]:


df1.isnull()


# In[48]:


df1.isnull().sum()


# In[49]:


df1.isnull().sum().sum()


# In[50]:


df5=pd.read_csv("k.csv")


# In[51]:


df6=df5.drop(['Unnamed: 14','Unnamed: 15'],axis=1)


# In[52]:


df6


# In[53]:


df6.isnull().sum()


# In[54]:


df6.isnull().sum().sum()


# In[55]:


df6.fillna(value=888)


# In[56]:


df6.fillna(method='pad')


# In[57]:


df6.fillna(method='bfill')


# In[58]:


df6


# In[59]:


df6.fillna(method='pad',axis=1)


# In[60]:


df6.fillna(method='pad',axis=0)


# In[61]:


df6


# In[62]:


df6.fillna({'age':9.9,'thal':10})


# In[63]:


df6.fillna(value=df6['age'].mean())


# In[64]:


df6.fillna(value=df6['age'].max())


# In[65]:


df6.dropna()


# In[66]:


df6.dropna(how='any')


# In[67]:


df6.dropna(how='all')


# In[68]:


df6.replace(to_replace=np.nan,value=df6['sex'].mean())


# In[69]:


df6.replace(to_replace=df6['age'][4],value=df6['sex'].mean())


# In[70]:


df6.isnull().mean()*5


# In[71]:


df1


# In[82]:


d=df1.head(100)


# In[83]:


x=d["age"]


# In[84]:


x


# In[85]:


y=d["chol"]


# In[86]:


y


# # Data Visualization

# # 1. Scatter plot

# In[87]:


mp.scatter(x,y)
mp.title("age vs chol")
mp.xlabel("Age")
mp.ylabel("chol")
mp.colorbar()
mp.show()


# # 2. Bar Plot

# In[88]:


mp.bar(x,y)
mp.title("bar diagram")
mp.show()


# # 3. Histogram

# In[89]:


mp.hist(x)
mp.show()


# # 4. barplot using seaborn package

# In[100]:


sb.barplot(x='age',y='chol',data=d,width=1.9)
mp.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




