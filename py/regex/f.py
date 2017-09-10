import re
a='happyhappyhappyhappyhappyhappy'
b=re.search('[happy{7}]',a)
if b == None:
    print('not found')
else:
    print('found')
