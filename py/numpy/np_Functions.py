import numpy as np
a=np.arange(100)
b=[1,2,3]
c=[4,5,6]
d=[b,c]
e=np.array(d)

print('ndim:',np.ndim(e))
print(e)
print('shape:',np.shape(e))
e=e.reshape(3,2)
print('shape:',np.shape(e))
print(e)
