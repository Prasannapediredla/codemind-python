a = int(input())
b = a*a
a= str(a)
a = a[::-1]
a = int(a)
c = a*a
c = str(c)
c =c[::-1]
c = int(c)
if b == c:
    print('True')
else:
    print('False')