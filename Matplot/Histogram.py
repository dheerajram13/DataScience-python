import random
import numpy as np
import matplotlib.pyplot as plt
rolls = []
for i in range(100):
    rolls.append(random.choice([1,2,3,4,5,6]))
plt.hist(rolls,bins = np.linspace(0.5,6.5,7))    
plt.show()    