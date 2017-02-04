import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imsave
from skimage import data,img_as_float, io, measure


a=np.ones((128,128))
b=np.zeros((128,5))

y=(1/x)
x=np.arrange(128)
fig=plt.figure()
plt.plot(x,y,'ro')

c=np.zeroes((64,5))


imsave('white.png', a)
imsave('line.png',b)
imsave('half.png',c)
imsave('curve.png',fig)

contours=measure.find_contours(a,0.8)
fig1,ax=plt.subplots()
ax.imshow(r,interpolation='nearest',cmap=plt.cm.gray)
for n, contour in enumerate(contours):
            ax.plot(contour[:1], contour[:,0], linewidth=2)


ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])

io.imshow(a)
io.imshow(b)
plt.show()

