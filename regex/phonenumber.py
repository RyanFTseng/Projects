l=["1","2",'3','4','5','6','7','8','9','0']
print('enter phone number')
x=input()
v =0
if '-' in x:
    a=x.split('-')
    if len(a)==3 and len(a[0]) == 3 and len(a[1]) == 3 and len(a[2]) == 4:
        for n in a:
            for m in n:
                if m not in l:
                    print('invalid phone number')
                    v = 1
    else:
        print('invalid phone number')
        v = 1
else:
    print('invalid phone number')
    v = 1

if v == 0:
    print("Valid")
                
