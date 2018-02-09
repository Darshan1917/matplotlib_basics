# this is a demo for barchart or bar graph and histogram
# author - Darshan

import matplotlib.pyplot as plt

# x=[2,4,6,8,10]
# y=[3,9,4,1,6]
# x1=[1,3,5,7,9]
# y1=[9,6,1,7,3]
# plt.bar(x,y,label="bar1")
# plt.bar(x1,y1,label="bar2")
# plt.legend()
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Demo Graph\npart-2")

#default value of color is blue we can change to anything we need
# histograms are useful when we have array of list
u = [41,78,25,12,56,88,96,45,43,99,100,85,21,24,55,64,33,27,102,111,71,66,19,29,66,74,54,95,88,39,64]
# we create bins for value ranges in histogram and we use this value to plot the hist
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120]

plt.hist(u,bins,histtype="bar",rwidth=0.7,label="hist")
plt.legend()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Demo Graph\npart-2")
plt.show()