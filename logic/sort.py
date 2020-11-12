import numpy as np
a=[1,5,2,12,15,56,22,11,34]
for n in range(0,len(a),1):
    for m in range(n,len(a),1):
        if a[n]>a[m]:
            q=a[m]
            a[m]=a[n]
            a[n]=q
b=np.array(a)
print(b)
        
        
            
