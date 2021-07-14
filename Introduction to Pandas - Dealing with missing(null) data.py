# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 05:18:09 2021

@author: abc
"""

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

print(df.head())

print(df.isnull())   #To know how many missing vallues we have 


######################################################################################

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df = df.drop('Manual2',axis = 1)   #delete the manual2 set

df2 = df.dropna() #it is delete null values of the dataset

print(df.head(25))
print(df2.head(25))

##################################################################################

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

print(df.isnull().sum())   #it is print how many number of data are missing

###############################################################################

#imputaion 

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df = df.drop('Manual2',axis = 1)

print(df['Manual'].describe)

print(df.head(25))


df['Manual'].fillna(100, inplace = True)  # It is fill the null values in the dataset

print(df.head(25))


##################################################################################

import pandas as pd
import numpy as np
df = pd.read_csv('manual_vs_auto.csv')

print(df.head(25))

# fill the missing value using  mean value of another three rows 
df['Manual'] = df.apply(lambda row: (round((row['Auto_th_2']+row['Auto_th_3']+row['Auto_th_4'])/3))
                        if np.isnan(row['Manual']) else row['Manual'], axis = 1)

           

print(df.head(25))


######################################################################################

                              #THANK YOU
                              #YADD HEE NA 
                              #GARR PEE RAHE SURKSIT RAHE
                              #AURR
                              #TWO GAJJ KI DURII HEE JARURI
                              
                              

























