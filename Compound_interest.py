p,r,t = map(int,input().split())
Ci = p*pow((1+r/100),t)
print(f"{Ci:.2f}")