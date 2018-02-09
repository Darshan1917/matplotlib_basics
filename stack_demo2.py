# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 20:11:41 2018

@author: dumapath
"""

# Stack plot are used to show Size of use or the relative percentage in a whole 
# This is used to convey a holistic number and in that full number sections that comprise the holistic number 


import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleeping=[7,8,6,11,7] 
eating =[3,1,5,3,2]
working =[7,8,7,1,3]
playing=[3,3,2,4,8]

# Generally comment the fake plots created below and run we dont know what each colour mean 

plt.plot([],[],color = 'r',label = "sleeping", linewidth=5)
plt.plot([],[],color = 'b',label = "eating", linewidth=5)
plt.plot([],[],color = 'g',label = "working", linewidth=5)
plt.plot([],[],color = 'k',label = "playing", linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing , colors =['r','b','g','k'] )

plt.scatter
plt.xlabel("X-axiz")
plt.ylabel("Y-axiz")
plt.title("Graph\nNew")
plt.show()

# stacks the plot one over the other and complets them 

