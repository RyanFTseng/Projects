import numpy as np
import matplotlib.pyplot as plt

from skimage import measure, io
x,y=np.ogrid[-np.pi:np.pi:100j, -np .pi:np.pi:100j]
#print(y)
r=np.sin(np.exp((np.sin(x)**3+np.cos(y)**2)))

#r=np.exp((np.sin(x)**3+np.cos(y)**2))
#print(r)
io.imshow(r)

contours=measure.find_contours(r,0.8)
fig,ax=plt.subplots()
ax.imshow(r,interpolation='nearest', cmap=plt.cm.gray)
for n, contour in enumerate(contours):
    ax.plot(contour[:,1],contour[:,0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])




plt.show()
