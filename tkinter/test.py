v='32+3-2='
l=list(v)
var=''
total=0
current_operation='+'
operate=0
for i in l:
      print(i,'i')
      print(total,'total')
      print(var,'var')
      
      if current_operation=='+' and operate==1:
            total=total+int(var)
            operate=0
            var=''
      if current_operation=='-'and operate==1:
            total=total-int(var)
            operate=0
            var=''
      if current_operation=='*'and operate==1:
            total=total*int(var)
            operate=0
            var=''
      if current_operation=='/'and operate==1:
            total=total/int(var)
            operate=0
            var=''
      if i in ['+','-','*','/','=']:
            operate=1
      else :
            var=var+i
print (total)


'''if '+' in v:
      l=v.split('+')
if '-' in l:
      a,b=v.split('-')

print(a)
print(b)'''

print(v)
