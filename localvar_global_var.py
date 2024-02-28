#!/usr/bin/env python
# coding: utf-8

# In[1]:


def drink():
    potion_strength=2
    print(potion_strength)
drink()
print(potion_strength)
#local variable and global variable
#local variable is defined within a function and global variable is defined everywhere.


# In[2]:


protein=10
def drink():
    potion_strength=2
print(protein)
drink()


# In[3]:


study_level=3
def createsubject():
    subjects=["DataSc","AI","ML"]
    if study_level<5:
        newsubject=subjects[0]
print(newsubject)
createsubject()


# In[4]:


#without function, all variables are by default taken as global variable. there is no problem with for or while loops. we have problem only with those operators which is defined with a colon.


# In[5]:


subjects=10
def increase_subject():
    s=10
    print(f"inside {subjects}")
    return s+2
increase_subject()
print(f"outside {increase_subject()}")


# In[6]:


def myfunc():
    for i in range(1,20):
        if i==20:
            print("you got")
myfunc()


# In[7]:


from random import randint


# In[8]:


dice_num=["0","1","2","3","4","5"]
dice_choice=randint(1,6)
print(dice_num[dice_choice])


# In[9]:


age=input("how old are you?:")
if age>18:
    print(f"age is {age}")


# In[11]:


pages=0
wordperpage=0
pages=int(input("no. of pages:"))
wordperpage=int(input("no. of words per page:"))
total=pages*wordperpage
print(total)


# In[12]:


#pythontutor.com is a debugging software


# In[13]:


def mutate(a_list):
    b_list=[]
    for item in a_list:
        newitem=item*2
        b_list.append(newitem)
    print(b_list)
mutate([1,2,3,5,8,13])


# In[ ]:




