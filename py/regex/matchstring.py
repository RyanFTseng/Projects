import re
a='hello 000 100 999 two three four 1000 2000 9999'
b=re.match('\s{5} \d{3} \d{3} \d{3} \s{3} \s{5} \s{4} \d{4} \d{4} \d{4}',a)
if a == None:
    print('not found')
else:
    print('found')
