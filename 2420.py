n = int(input())
a = list(map(int, input().split()))[:n]
aux = int(sum(a)/2)
add = 0
for i in range(n):
    add += a[i]
    if add == aux:
        print(i+1)
        break