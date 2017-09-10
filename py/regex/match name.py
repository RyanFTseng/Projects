import re
a='ryan tseng qwe ert'
b=re.search('ryan',a).span()
print(b)
if b[0] != 0:
    print('not found')
else:
    print('found')
 
