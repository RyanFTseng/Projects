import re
a=re.match('youngwonks|raspberrypi','youngwonks is a great place to learn raspberrypi')
b=re.match('raspberrypi|youngwonks','raspberrypi is fun to learn at youngwonks')
print(a.group())
print(b.group())
