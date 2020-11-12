def f(a):
    if a<2:
        return(a)
    else:
        return f(a-1)+f(a-2)

for n in range(1,100):
    print(f(n))
 
