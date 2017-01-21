from skimage import io
from skimage import data, io, filters
from skimage import color
from skimage import img_as_float
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
img=io.imread('/home/ubuntuu/ywryantseng/imgpr/butterfly.jpg',as_grey=True)
global_thresh=filters.threshold_otsu(img)
print(type(global_thresh), img.shape,img)
binary_global=img>global_thresh
block_size=41
binary_adaptive=filters.threshold_adaptive(img,block_size,offset=10)
fig,(ax1,ax2,ax3)=plt.subplots(ncols=3,figsize=(16,16),sharex=True,sharey=True)
ax1.imshow(img)
#ax2.imshow(binary_global)
ax3.imshow(binary_adaptive)
ax1.set_adjustable('box-forced')
ax2.set_adjustable('box-forced')
ax3.set_adjustable('box-forced')
plt.show()
