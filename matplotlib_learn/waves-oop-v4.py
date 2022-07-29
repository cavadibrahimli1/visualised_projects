import matplotlib.pyplot as plt
import numpy as np

fig,axes = plt.subplots(figsize=(15,15))

t= np.linspace(0,10,100)

# Lin width options
axes.plot(t, np.sin(t) + 1, color="blue", lw = 0.25)
axes.plot(t, np.sin(t) + 2, color="blue", lw = 1)
axes.plot(t, np.sin(t) + 3, color="blue", lw = 5)
axes.plot(t, np.sin(t) + 4, color="blue", lw = 9)
# Line Style options
axes.plot(t, np.sin(t) + 6, color="purple", lw = 5, ls ='-')
axes.plot(t, np.sin(t) + 7, color="purple", lw = 5, ls ='-.')
axes.plot(t, np.sin(t) + 8, color="purple", lw = 5, ls =':')
# Markers options
axes.plot(t, np.sin(t) + 10, color="red", lw = 0.1, ls='-', marker='s')
axes.plot(t, np.sin(t) + 11, color="red", lw = 0.1, ls='-', marker='o')
axes.plot(t, np.sin(t) + 12, color="red", lw = 0.1, ls='-', marker='*')
axes.plot(t, np.sin(t) + 13, color="red", lw = 0.1, ls='-', marker='+')
# marker size and color
axes.plot(t, np.sin(t) + 15, color="green", lw=1, ls='-', marker='o', markersize=3)
axes.plot(t, np.sin(t) + 16, color="green", lw=1, ls='-', marker='o', markersize=7)
axes.plot(t, np.sin(t) + 17, color="green", lw=1, ls='-', marker='s', markersize=10, markerfacecolor="yellow")
axes.plot(t, np.sin(t) + 18, color="green", lw=1, ls='-', marker='^', markersize=10, markerfacecolor="orange", markeredgewidth=2, markeredgecolor="blue");

plt.show()
