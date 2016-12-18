import re
pattern="sim|nothing"
a=re.match(pattern,'simple is awesome!!')
b=re.match(pattern,'similar to me!!')
c=re.match(pattern,'simulation testing!!')
d=re.match(pattern,'nothing!!')
print(a.group())
print(b.group())
print(c.group())
print(d.group())
