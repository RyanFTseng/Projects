
import re
pattern="[\w+]"
a=re.match(pattern,'the adventures of superman')
b=re.match(pattern,'the adventures of superwoman')
c=re.match(pattern,'the adventures of batman')
print(a.group())
print(b.group())
print(c.group())
