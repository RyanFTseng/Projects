def p(n):
    if n==1:
        return [[1]]
    else:
        x=[1]
        y=p(n-1)
        z=y[-1]
        for i in range(len(z)-1):
            x.append(z[i]+z[i+1])
        x=x+[1]
        y.append(x)
        return y
        

print(p(6))
        




    
