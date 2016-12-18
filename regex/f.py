import re
a='happyhappyhappyhappyhappy'
b=re.match('happy',a).span()
print(b)
if b == None:
    print('not found')
else:
    print('found')

