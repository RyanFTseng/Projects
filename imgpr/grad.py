from skimage import io
from skimage import data, io, filters
from skimage import color
from skimage import img_as_float
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

hue_gradient=np.linspace(0,1)
hsv=np.ones(shape=(1,len(hue_gradient),3),dtype=float)
hsv[:,:,0]=hue_gradient
all_hues=color.hsv2rgb(hsv)
fig,ax=plt.subplots(figsize=(5,2))
ax.imshow(all_hues,extent=(0,1,0,0.2))
ax.set_axis_off()
plt.show()
