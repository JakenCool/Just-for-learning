import numpy as np
import matplotlib.pyplot as plt

#将图形平移，可以使得某一部分画在图形中央

a=[0,1,2,3]
b=np.roll(a,1)#b = [3 0 1 2]

plt.xticks(a,b) #将x坐标的a换成b
plt.plot(a,b)