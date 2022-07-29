from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(20,15))
ax= fig.gca(projection="3d")

X = np.arange(-5,5,0.25)
Y = np.arange(-5, 5,0.25)
X, Y = np.meshgrid(X,Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap= cm.coolwarm)
plt.show()
