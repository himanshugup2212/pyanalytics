# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:42:22 2020

@author: Himanshu Gupta
"""
import pandas as pd
import statsmodels.api as sm
dataset_mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
mtcars = dataset_mtcars.data
print(mtcars.head(4))
print(mtcars.tail(4))
print("No. of rows: ",mtcars.index.size)
print("No. of columns: ",mtcars.columns.size)
print("Columns: ",mtcars.columns)
print(mtcars[mtcars['cyl']==8])
print(mtcars[mtcars['mpg']<=27])
print(mtcars.iloc[[0,3,6,24],[0,5,6]])
print(mtcars.iloc[25:-3])
print(mtcars.iloc[0::2,0::2])
print(mtcars.loc["Mazda RX4 Wag",["cyl", "am"]])
for i in range(0,len(mtcars.index),1):
    if mtcars.index[i]=="Merc 280":
        start=i
    if mtcars.index[i]=="Volvo 142E":
        end=i
print(mtcars.iloc[start+1:end][["cyl", "am"]])
print(mtcars[(mtcars['mpg']>23) | (mtcars['wt']<2)])
