#!/usr/bin/env python
# coding: utf-8

# Next day Lab work: 23.11.23
# 
#  matrix algebra,
# Eigen values and eigen vectors, eigen decomposition, singular value decomposition.

# In[1]:


import numpy as np


# In[2]:


M1=np.matrix([
            [1,2,1],
            [0,1,0],
            [1,5,1]])
M2=np.matrix([
            [2,5,9],
            [1,2,7],
            [1,8,0]])
print(M1)
print("\n",M2)


# # Matrix Multiplication

# In[3]:


product=np.dot(M2,M1)
print(product)


# # Matrix Addition

# In[4]:


Sum=np.add(M1,M2)
print(Sum)


# In[5]:


difference=np.subtract(M2,M1)
print(difference)


# # Eigenvalues and Eigenvectors

# In[6]:


e1,e2=np.linalg.eig(M1)
eval1=np.round(e1,1)
evec1=np.round(e2,1)
E1,E2=np.linalg.eig(M2)
eval2=np.real(np.round(E1,1))
evec2=np.real(np.round(E2,1))
print(f"Eigenvalues of matrix M1 are:{eval1}")
print(f"Eigenvectors of matrix M1 are:\n{evec1}")
print(f"Eigenvalues of matrix M2 are:{eval2}")
print(f"Eigenvectors of matrix M2 are:\n{evec2}")


# # Eigen Decomposition

# In[7]:


P=np.matrix(evec1)
D=np.diag(eval1)
P_inv=np.linalg.inv(P)
PD=np.dot(P,D)
A=np.dot(PD,P_inv)
print(f"The original matrix is:\n {M1} \n and the decomposed matrix is:\n{A}")


# In[8]:


Q=np.matrix(evec2)
E=np.diag(eval2)
Q_inv=np.round(np.linalg.inv(Q),1)
QE=np.dot(Q,E)
B=np.round(np.dot(QE,Q_inv),0)
print(f"The original matrix is:\n {M2} \n and the decomposed matrix is:\n{B}")


# # Singular Value Decomposition

# In[9]:


import scipy
U,S,v=scipy.linalg.svd(M1)
print("M1=USV',where:\n")
print(f"U={np.round(U,1)}")
print(f"\n S={np.round(S,1)}")
print(f"\n V'={np.round(v,1)}")

