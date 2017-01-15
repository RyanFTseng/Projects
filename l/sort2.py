a=['a','z','b','d','aa','ab']
for n in range(0,len(a),1):
    for m in range(n,len(a),1):
        if a[n]>a[m]:
            q=a[m]
            a[m]=a[n]
            a[n]=q
b=np.array(a)
print(b)
