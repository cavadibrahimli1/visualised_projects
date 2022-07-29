import numpy as np
import matplotlib.pyplot as plt

# Create a new figure window
fig = plt.figure()

# Add new axes
axes = fig.add_axes([0,0,1,1])

x = np.linspace(0,10,100)
y = np.sin(x)

axes.plot(x,y,"r--", label= "Red Sine Wave #1")
axes.set_xlabel("Time")
axes.set_ylabel("Sine Wave")
axes.set_title("My first Plot!")
axes.legend()
axes.set_ylim([-1,1])
axes.set_xlim([0,10])
axes.grid()

plt.show()
