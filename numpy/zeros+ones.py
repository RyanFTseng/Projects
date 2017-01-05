import numpy as np
a=np.ones(10)
print(a)
b=np.zeros(10)
print(b)

c=[1,2,3]
d=[4,5,6]
e=[c,d]
x=np.array(e)
print(x)
print(np.zeros_like(x))
print(np.ones_like(x))
