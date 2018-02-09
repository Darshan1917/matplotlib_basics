# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 20:57:54 2018

@author: dumapath
"""

#pie Charts
# 360 
import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleeping=[7,8,6,11,7] 
eating =[3,1,5,3,2]
working =[7,8,7,1,3]
playing=[3,3,2,4,8]

slices  = [7,2,5,13]
activity = ['sleeping','eating','working','playing']
explode = (0.1, 0.3, 0, 0) # to pull out a part of pie
# autopct is used to give percentages
plt.pie(slices,labels=activity,shadow=True,explode=explode,autopct='%.1f%%') # try :%.1f%%,%.2f%%
plt.title("Pie chart")
plt.show()