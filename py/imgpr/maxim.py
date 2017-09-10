from scipy import ndimage as ndi
import matplotlib.pyplot as plt
from skimage.feature import peak_local_max
from skimage import data,img_as_float, io

im=io.imread('/home/ubuntuu/ywryantseng/imgpr/grayscale.jpg',as_grey=True)

image_max=ndi.maximum_filter(im, size=20, mode= 'constant')
coordinates=peak_local_max(im,min_distance=20)

fig,ax=plt.subplots(1,3, figsize=(16,6), sharex=True, sharey=True, subplot_kw={'adjustable':'box-forced'})
ax1,ax2,ax3=ax.ravel()
ax1.imshow(im,cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('original')

ax2.imshow(image_max,cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('max filter')

ax3.imshow(im,cmap=plt.cm.gray)
ax3.autoscale(False)
ax3.plot(coordinates[:,1], coordinates[:,0],'r')
ax3.axis('off')
ax3.set_title('peak local max')

fig.subplots_adjust(wspace=0.02,hspace=0.02,top= 0.9,bottom=0.02,left=0.02,right=0.98)

plt.show()
