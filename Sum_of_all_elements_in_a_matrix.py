r,c  = map(int, input().split()) #reading rows 
mat = []
for i in range(r):
    inner_list = list(map(int, input().split()))[:c:]
    mat.append(inner_list)
s  = 0
# Elementry based looping
for inner_list in mat:
    for every_value in inner_list:
        s += every_value
print(s)