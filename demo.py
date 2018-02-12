# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 17:29:39 2018

@author: dumapath
"""

import matplotlib.pyplot as plt

x = [0,1,2,3,4,5]
y = [10,20,15,18,7,19]
xlabels = ['jan','feb','mar','apr','may','jun']

xlabelsnew = []
for i in xlabels:
    if i in []:
        i = ' '
        xlabelsnew.append(i)
    else:
        xlabelsnew.append(i)
        
plt.plot(x,y)
plt.xticks(range(0,len(x)),xlabelsnew,rotation=45)
plt.show()