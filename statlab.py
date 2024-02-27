#!/usr/bin/env python
# coding: utf-8

# # Q1. Let X={1,2,3,4,5} and X~Bin(5,0.3). Find mean, variance, skewness and kurtosis for the distribution. Also find pmf and cdf.

# In[1]:


from scipy.stats import binom as b

n=5
p=0.3

mean,var,sk,kt=b.stats(n,p,moments='mvsk')

x=list(range(n+1))

cdf=b.cdf(x,n,p)

pmf=b.pmf(x,n,p,loc=0)


# In[2]:


print(f"mean(X)={mean}\nvar(X)={var}")
print(f"\nskewness(X)={sk}\nkurtosis(X)={kt}")
print(f"\npmf of X is given by:\nf(x)={pmf}\nfor x={x} respectively")
print(f"\ncdf of X is given by:\nF(x)={cdf}\nfor x={x} respectively")


# # Q2. Let X~Poisson(mu=3). Find the probability that the rv assumes the values: 
#     (i) 0,1,2,3        (ii) less than 3       (iii) at least 2
# 

# In[3]:


from scipy.stats import poisson as p

mu=3

#Probability that X takes the values 0,1,2,3
x1=list(range(4))
prob=list(p.pmf(x1,mu))

#Probability that X<3
prob3=p.cdf(2,mu)

#Probability that X>=2
prob2=1-p.cdf(2,mu)


# In[4]:


for i in x1:
    print(f"\nP[X={i}]={prob[i]}")
    
print(f"\nP[X<3]={prob3}")
print(f"\nP[X>=2]={prob2}")


# # Q3. The mean weight of 500 male students at a certain village is 151 lbs and the sd is 15 lbs. Assuming that the weights are normally distributed calculate the % of students with weight more than 155 lbs

# In[5]:


from scipy.stats import norm as n


#sample size=500
mu=151 #mean
sigma=15 #sd
w=155

#Percentage of students with X>=155
Z=(w-mu)/sigma
pct=(1-n.cdf(Z))*100

print(f"Percentage of students having weight more than 155 lbs={pct}")

