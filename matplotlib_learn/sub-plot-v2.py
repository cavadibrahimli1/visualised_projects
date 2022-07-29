import numpy as np
import matplotlib.pyplot as plt


t= np.arange(0.,5.,0.2)

plt.subplot(3,1,1)
plt.plot(t,t,"r--");

plt.subplot(3,1,2)
plt.plot(t, t**2, "bs")

plt.subplot(3,1,3)
plt.plot(t,t**3,"g^");

plt.show()
