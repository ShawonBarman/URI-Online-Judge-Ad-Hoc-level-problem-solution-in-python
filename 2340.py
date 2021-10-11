import math
n = int(input())
maxi = -9999999
id = 0
for i in range(n):
    d, c = input().split()
    aux = int(c)*math.log10(int(d))
    if aux > maxi:
        maxi = aux
        id = i
print(id)