#!/usr/bin/env python
# coding: utf-8

# # Practical home work: 12.01.2024

# # 1. Check whether a matrix is LU factorizable or not, and solve the system of linear equation through LU decomposition

# In[1]:


import numpy as np
from scipy.linalg import lu_factor,lu_solve,lu


# In[2]:


A=np.array([[2,-3,4],[1,1,4],[3,4,-1]])
b=np.array([8,15,8])


# In[3]:


P,L,U=lu(A)
A_=np.dot(P, np.dot(L, U))


# In[4]:


print(f"\nA:\n{A}")
print(f"\nnewA:\n{A_}")
print(f"Permutation matrix:\n{P}")
print(f"Lower triangular matrix:\n{L}")
print(f"Upper triangular matrix:\n{U}")


# In[5]:


lu_solve(lu_factor(A),b)


# # 2. Find orthogonal basis of vector through Gram-schmidt orthogonalization

# # 3. QR factorization of that matrix.

# In[6]:


X = np.array([[2,-3,4],
            [1,1,4],
            [3,4,-1]])
Q,R=np.linalg.qr(X, mode='complete')
QR=np.dot(Q,R)
print(f"X=\n{X}\n")
print(f"orthogonal basis space of X=\n{Q}\n")
print(f"R=\n{R}\n")
print(f"QR=X=\n{QR}")

