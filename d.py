print('input')
a=int(input())
b=a
for n in range(0,a-1,1):
    a=a*(b-1)
    b=b-1
print(a)
