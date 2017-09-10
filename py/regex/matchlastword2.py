import re
pattern="man"
a=re.search(pattern,'the adventures of superman').span()
b=re.search(pattern,'the adventures of superwoman').span()
c=re.search(pattern,'the adventures of batman').span()
d=re.search(pattern,'the adventures of superwowowowoman').span()
print(a)
print(b)
print(c)
print(d)
if a[0] != 23 and b[0]!=25 and c[0]!=21 and d[0]!=31:
    print('not found')
else:
    print('found')
