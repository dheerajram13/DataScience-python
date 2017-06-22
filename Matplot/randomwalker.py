import numpy as np
import matplotlib.pyplot as plt

delta_x = np.random.normal(0,1,(2,5))
x = np.cumsum(delta_x,axis = 1)
plt.plot(x[0],x[1],"rd-")
plt.show()