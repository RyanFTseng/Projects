import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imsave
from skimage import data,img_as_float, io

a=np.ones((128,128))
b=np.zeros((128,5))


imsave('white.png', a)
imsave('line.png',b)



io.imshow(b)
plt.show()

