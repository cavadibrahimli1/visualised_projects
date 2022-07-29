import matplotlib.pyplot as plt
import numpy as np

np.random.seed(20)

data_1= np.random.normal(200,20,2000)
data_2= np.random.normal(60,30,2000)
data_3= np.random.normal(70,20,2000)
data_4= np.random.normal(40,5,2000)

data_all = [data_1,data_2,data_3,data_4]

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
bp = ax.boxplot(data_all)

plt.show()
