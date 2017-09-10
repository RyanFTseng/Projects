import re

f=open('test.txt','r')
for n in f:
    a,b,c,d,e,f=n.split(  )

x=re.match('\d{3}-\d{3}-\d{4}',a)
if x==None:
    print('not found')
else:
    print('found')

y=re.match('[\w]+@[\w]+.[\w]+',c)
if y==None:
    print('not found')
else:
    print('found')

z=re.match('http://www.+[\w]+.[\w]',e)
if z==None:
    print('not found')
else:
    print('found')

q=re.match('\d{2}:\d{2}:\d{2}:\d{2}:\d{2}',f)
if q==None:
    print('not found')
else:
    print('found')
