from skimage import io
from skimage import data, io, filters
from skimage import color
from skimage import img_as_float
import matplotlib
from matplotlib import pyplot as plt
grayscale_image=io.imread('/home/ubuntuu/ywryantseng/imgpr/index.jpeg')
#image=color.gray2rgb(grayscale_image)
red_multiplier=[3,0,0]
yellow_multiplier=[5,23,5]
blue_multiplier=[11,1,20]
green_multiplier=[0,3,0]
fig,(ax1,ax2,ax3,ax4)=plt.subplots(ncols=4,figsize=(8,4),sharex=True,sharey=True)
ax1.imshow(grayscale_image*red_multiplier)
ax2.imshow(grayscale_image*yellow_multiplier)
ax3.imshow(grayscale_image*blue_multiplier)
ax4.imshow(grayscale_image*green_multiplier)
ax1.set_adjustable('box-forced')
ax2.set_adjustable('box-forced')
ax3.set_adjustable('box-forced')
ax4.set_adjustable('box-forced')
plt.show()

##img=io.imread('/home/ubuntuu/ywryantseng/imgpr/index.jpeg')
##img2=io.imread('/home/ubuntuu/ywryantseng/imgpr/index.jpeg',as_grey=True)
##image=data.coins()
##edges=filters.sobel(image)
###io.imshow(edges)
##print(img2.shape)
##plt.imshow(img2)
##plt.show()

