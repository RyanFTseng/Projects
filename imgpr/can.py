from skimage.feature import canny
from scipy import ndimage as ndi
from skimage import data, io, filters
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
img=io.imread('/home/ubuntuu/ywryantseng/imgpr/grayscale.jpg',as_grey=True)
coins=data.coins()
edges=canny(img)
fig,(ax1,ax2,ax3)=plt.subplots(ncols=3,figsize=(16,16),sharex=True,sharey=True)
fill_coins=ndi.binary_fill_holes(edges)

ax1.imshow(img)
ax2.imshow(edges)
ax3.imshow(fill_coins)
ax1.set_adjustable('box-forced')
ax2.set_adjustable('box-forced')
ax3.set_adjustable('box-forced')
plt.show()
