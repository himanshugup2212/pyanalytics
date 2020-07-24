# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:05:00 2020

@author: Himanshu Gupta
"""
import pandas as pd
import numpy as np
data=pd.read_csv("denco.csv")
data1=data.groupby("custname").size().sort_values(ascending=False)
data1.name="frequency"
data2=data.groupby("custname")["revenue"].sum().sort_values(ascending=False)
data2.name="sum of revenue"
data3=data.groupby("partnum")["revenue"].sum().sort_values(ascending=False)
data3.name="sum of revenue"
data4=data.groupby("partnum")["margin"].sum().sort_values(ascending=False)
data4.name="sum of margin"
#%%
writer = pd.ExcelWriter('Denco_Sol.xlsx', engine='xlsxwriter')
data1.head(10).to_excel(writer,header=1,sheet_name='Sheet1')
data2.to_excel(writer,header=1,sheet_name='Sheet2')
data3.to_excel(writer,header=1,sheet_name='Sheet3')
data4.to_excel(writer,header=1,sheet_name='Sheet4')
writer.save()
