import numpy as np
c=[1,2,3]
d=[4,5,6]
e=[c,d]
m=np.array(e)
print('m:',m)
z=np.array(m[::-1,::-1])
print('z:',z)
x=np.array(m[::2,::2])
print('x:',x)
y=np.array(m[::1,::-3])
print('y:',y)
a=np.array(m[::1,::3])
print('a:',a)
