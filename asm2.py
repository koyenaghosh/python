# -*- coding: utf-8 -*-
"""asm2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NQWxr-taAID8ApcLThCuNiGRFA225bpG
"""

import pandas as pd

df=pd.read_csv('QueryResults.csv',names=['Date','Tag','Posts'],header=0)

df

df.isnull().sum()

df.groupby('Tag').count()

df.info()

type(df['Date'][1])

df.date=pd.to_datetime(df.Date)

df.date

r_df=df.pivot(index='Date',columns='Tag',values='Posts')

r_df

df1=r_df.fillna(0)



df1.index=pd.to_datetime(df1.index)

import matplotlib.pyplot as plt

plt.figure(figsize=(16,10))
plt.xticks(rotation=90)
plt.xlabel('Date',fontsize=14)
plt.ylabel('No.of Posts',fontsize=14)
for i in df1.columns:
  plt.plot(df1.index,df1[i],label=df1[i].name)
plt.legend(fontsize=16)

df1['java'].name

roll_df=df1.rolling(window=20).mean()

plt.figure(figsize=(16,10))
plt.xticks(rotation=90)
plt.xlabel('Date',fontsize=14)
plt.ylabel('No.of Posts',fontsize=14)
for i in roll_df.columns:
  plt.plot(roll_df.index,roll_df[i],label=roll_df[i].name)
plt.legend(fontsize=16)
