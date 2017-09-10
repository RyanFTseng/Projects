import matplotlib
from matplotlib import pyplot as plt
import numpy as np
x=np.arange(100)
y=x**(1/2)
fig=plt.figure()
plt.plot(x,y,'ro')
plt.ylabel('some numbers')
plt.plot(x,y,linewidth=5.0)
plt.show()

