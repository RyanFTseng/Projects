import re
a='hello 000 100 999 two three four 1000 2000 9999'
b=re.search('000|100|999|1000|2000|9999',a)
if b == None:
    print('not found')
else:
    print('found')
