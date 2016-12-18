import re
print('enter number')
x=input()
a=re.match('\d{3}-\d{3}-\d{4}',x)
if a == None:
    print('not found')
else:
    print('found')
