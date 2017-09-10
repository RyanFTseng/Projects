v='3+3*3='
l=list(v)
var=''
total=0
operate=0
print(l)
ltotal=[]
ltotal.append(0)
for i in l:
      if i in ['+','-','*','/','=']:
            ltotal.append(var)
            var=''
            ltotal.append(i)
      else:
            var=var+i
      print(i,'i')
      print(total,'total')
      print(var,'var')
print (total)
print(ltotal,'ltotal')
total=0
operation='+'
if ltotal[1]=='':
      ltotal.pop(1)
for i in ltotal:
      if i in ['+','-','*','/','=']:
            operation=i
      else:
            if operation=='+':
                  total=total+int(i)
                  print(total)
            if operation=='-':
                  total=total-int(i)
                  print(total)
            if operation=='*':
                  total=total*int(i)
                  print(total)
            if operation=='/':
                  total=total/int(i)
                  print(total)
            if operation=='=':
                  total=int(i)
            
            
