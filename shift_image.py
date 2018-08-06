import numpy as np
import matplotlib.pyplot as plt

#将图形平移，可以使得某一部分画在图形中央

a=[0,1,2,3]
b=np.roll(a,1)
print(b)
plt.xticks(a,b)
plt.plot(a,b)