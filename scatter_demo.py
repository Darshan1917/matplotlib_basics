import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9]
y=[5,7,1,9,0,2,1,6,8]
# use google for color and marker types in matplotlib
plt.scatter(x,y,label='skat',color='Green' ,marker='*',s=500)
plt.legend()
plt.xlabel("X-axiz")
plt.ylabel("Y-axiz")
plt.title("Graph\nNew")
plt.show()