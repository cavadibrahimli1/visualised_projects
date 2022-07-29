import matplotlib.pyplot as plt
import numpy as np


#Create a new figure
fig = plt.figure()

x = np.linspace(0, 10, 100)
y = np.sin(x)

axes1= fig.add_axes([0,0,1,1]) #main axes
axes2= fig.add_axes([0.1,0.2,0.5,0.5]) #insert axes
axes3= fig.add_axes([0.5,0.2,0.5,0.5]) #insert axes

#Larger Figure Axes 1
axes1.plot(x, y, 'b')
axes1.set_xlabel('X_label_axes1')
axes1.set_ylabel('Y_label_axes1')
axes1.set_title('Axes 1 Title');

# Insert Figure Axes 2
axes2.plot(x, y**2, 'r')
axes2.set_xlabel('X_label_axes2')
axes2.set_ylabel('Y_label_axes2')
axes2.set_title('Axes 2 Title');

# Insert Figure Axes 3
axes3.plot(x, y**2, 'g')
axes3.set_xlabel('X_label_axes3')
axes3.set_ylabel('Y_label_axes3')
axes3.set_title('Axes 3 Title');

plt.show()
