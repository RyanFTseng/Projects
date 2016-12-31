a=1
b=1
c=0

print('input #')
x=int(input())

if x==1:
    print(a)
if x==2:
    print(a)
    print(b)
elif x>2:
    print(a)
    print(b)
    for n in range(2,x,2):
        print(a+b)
        a=a+b
        print(a+b)
        b=a+b
