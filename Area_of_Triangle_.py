a,b,c=map(int,input().split())
s=(a+b+c)/2
import math
Area= math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"{Area:.2f}")