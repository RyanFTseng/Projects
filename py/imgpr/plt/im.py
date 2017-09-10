import matplotlib
from matplotlib import pyplot as plt1
from matplotlib import pyplot as plt2
import matplotlib.image as mping
import numpy as np
img=mping.imread('index.jpeg')
x=(img[::])
print('ndim:',np.ndim(x))
print('shape:',np.shape(x))
x=x.reshape(275,183,3)
plt1.imshow(x)
plt1.show()

