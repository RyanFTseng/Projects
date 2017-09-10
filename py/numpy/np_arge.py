import numpy as np
import time


def f1():
    t1=time.time()
    x=range(1000000)
    a=range(1000000)
    c=[]
    for n in range(0,1000000,1):
        c.append(a[n]+x[n])
    t2=time.time()
    x1=t2-t1
    return(x1)
    
    
def f2():
    t1=time.time()
    y=np.arange(1000000)
    b=np.arange(1000000)
    d=y+b
    t2=time.time()
    x2=t2-t1
    return(x2)
    

p=f1()
o=f2()
print(p-o)
