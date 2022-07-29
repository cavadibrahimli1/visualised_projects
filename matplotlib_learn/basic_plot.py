import numpy as np
import matplotlib.pyplot as plt

"""
0 equals start point.
10 quals end point.
0.2 equals intervals.
"""
x = np.arange(0,10,0.2)
print(x )
print("\n \n \n")

"""
Changing all values according to sin().
"""
y= np.sin(x)
print(y)

# Plot


plt.plot(x,y)
plt.xlabel("Time")
plt.ylabel("Sine Wave")
plt.title("Wave")

plt.show()
