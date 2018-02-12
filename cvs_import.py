# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:48:01 2018

@author: dumapath
"""
import csv
import numpy as np
import matplotlib.pyplot as plt

#PART 1
'''
x=[]
y=[]
with open("data1.txt",'r') as data:
    plots = csv.reader(data, delimiter=',')
    for row in plots:
        x.append(int(row[2]))
        y.append(int(row[3]))
'''  


# Past 2

x , y = np.loadtxt('data1.txt',delimiter=',',unpack = True,usecols =(2,3))
      
plt.plot(x,y,label="Loaded from file", color = 'Red')
#plt.bar(x,y,label="Loaded from file")
plt.margins(0.1)
plt.legend()
plt.xlabel("X-axiz : years ")
plt.ylabel("Y-axiz : population")
plt.title("Caribbean small states")
plt.show()
