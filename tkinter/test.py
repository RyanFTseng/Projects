v='32+3-2='
l=list(v)
var=''
total=0
current_operation='+'
operate=0

ltotal=[]
for i in l:

      
      '''if current_operation=='+' and operate==1:
            total=total+int(var)
            
            print('________________________',total)
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
      '''
      if i in ['+','-','*','/','=']:
            ltotal.append(var)
            var=''
            ltotal.append(i)
            print(ltotal)
            
            
            '''
            #operate=1
            current_operation=i
            if i=='+':
                  total=total+int(var)
                  var=''
            if i=='-':
                  total=total-int(var)
                  var=''
            total=total+int(var)
            var=
            '''
      
      else :
            var=var+i
      print(i,'i')
      print(total,'total')
      print(var,'var')
print (total)


'''if '+' in v:
      l=v.split('+')
if '-' in l:
      a,b=v.split('-')

print(a)
print(b)

print(v)'''
