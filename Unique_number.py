n = int(input())
x,f=[],0
while n!=0:
    x.append(n%10)
    n//=10
for i in x:
    if x.count(i)>1:
        f=1
        break
if f == 1:
    print("Not Unique Number")
else:
    print("Unique Number")
