import matplotlib.pyplot as plt
import numpy as np


mu= 20 # mean of distribution
sigma = 3 #standard deviation of distribution
x = mu + sigma * np.random.randn(1000)

num_bins= 30
n,bins, patches= plt. hist(x,num_bins, facecolor="green",alpha=0.5)

plt.ylabel("Probability")
plt.title(r"Histogram : $\mu=20$, $\sigma=3$")

plt.show()
