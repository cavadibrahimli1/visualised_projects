import numpy as np
import matplotlib.pyplot as plt

t= np.arange(0.,5.,0.2)
"""
0 refers to start point of figure
5 refers to end point of figure
0.2 refers to intervals.
"""
plt.plot(t, t, "r--", t, t**2, "b*",t , t**3, "g^", linewidth= 5.0)

plt.show()
