import numpy as np
import matplotlib.pyplot as plt


a=[0,1,2,3]
b=np.roll(a,1)
print(b)
plt.xticks(a,b)
plt.plot(a,b)