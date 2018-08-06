import numpy as np
import matplotlib.pyplot as plt

#这种方法比较有层次
fig = plt.figure(figsize=(5,2))#要画图了
ax1 = fig.add_subplot(111)#加入第一个subplot
t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line,  = ax1.plot(t, s, color='blue', lw=2)#line 是一个LinearD的object