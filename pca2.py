#!/usr/bin/env python
# coding: utf-8

# # Q1.Apply Gram-Schmidt Orthogonalisation to find orthogonal basis of v1=(1,1,1,0),v2=(0,1,1,1),v3=(0,0,1,1),v4=(0,0,3,0). Which are the column vectors of A? Find Q,R such that A=QR

# In[1]:


import numpy as np
X = np.array([[1,0,0,0],
            [1,1,0,0],
            [1,1,1,3],
            [0,1,1,0]])
Q,R=np.linalg.qr(X, mode='complete')
QR=np.dot(Q,R)
print(f"X=\n{X}\n")
print(f"orthogonal basis space of X=\n{Q}\n")
print(f"R=\n{R}\n")
print(f"QR=X=\n{QR}")
print(f"Q=\n{Q}\n")


# # Q2. If 3% of the bolts manufactured by a company are defective, what is the probability that in a sample of 200 bolts,5 will be defective ?(Apply proper distribution to find the value) 

# In[2]:


#n=200, p=0.03
#np=mu=6
#X~Poi(6)
from scipy.stats import poisson as p

mu=6

#Probability that X = 5
prob=p.pmf(5,mu)
print(f"probability that in a sample of 200 bolts,5 will be defective={prob}")


# # Q3. Assume the mean height of soldiers to be 68.22 inches with a variance of 10.8 sq. inches. How many soldiers in a regiment of 1000 would you expect to be over 6ft tall?

# In[5]:


from scipy.stats import norm as n


#sample size=1000
mu=68.22 #mean
sigma=10.8**0.5 #sd
w=72

#Percentage of students with X>72
Z=(w-mu)/sigma
pct=(1-n.cdf(Z))*1000
print(f"Number of soldiers having height over 6ft={np.round(pct,0)}")

