b=0


print('input')
a=int(input())
for n in range(2,a-1,1):
    if a%n==0:
        b=1
        break
        
if b==1:
    print('not prime')
if b==0:
    print('prime')
