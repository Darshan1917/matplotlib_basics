import matplotlib.pyplot as plt

x=[1,5,6,7]
y=[6,8,4,7]
x2=[0,3,9,1]
y2=[1,2,9,7]
plt.plot(x,y,label="First")

plt.plot(x2,y2,label="second")

# adding the titles and legends and labels
plt.title('Graph example\ncheck it')
plt.legend()
plt.xlabel('X-aixs')
plt.ylabel('Y-axis')
plt.show()