n = int(input())
temp = n
rev = 0
if n<0:
    n = abs(n)
    while(n!=0):
        rem = n%10
        rev = rev*10+rem
        n = n//10
    print(-abs(rev))
else:
    while(n!=0):
        rem =n%10
        rev = rev*10+rem 
        n = n//10
    print(rev)