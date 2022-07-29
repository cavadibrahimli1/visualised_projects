import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, axes = plt.subplots(nrows = 3, ncols = 1, figsize=(10,10))

# Use axes object to add elements to plot
axes[0].plot(x, y, 'r')
axes[0].set_xlabel('x1')
axes[0].set_ylabel('y1')
axes[0].set_title('title 1');

axes[1].plot(x, y**2, 'b')
axes[1].set_xlabel('x2')
axes[1].set_ylabel('y2')
axes[1].set_title('title 2');

axes[2].plot(x, y**3, 'b')
axes[2].set_xlabel('x3')
axes[2].set_ylabel('y3')
axes[2].set_title('title 3');

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.4)
plt.show()
