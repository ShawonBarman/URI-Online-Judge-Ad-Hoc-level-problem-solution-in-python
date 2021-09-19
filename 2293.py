n, m = input().split()
arr = []
for i in range(int(n)):
    x = list(map(int, input().split()))[:int(m)]
    arr.append(x)
maxi = -999999
for i in range(int(n)):
    sum = 0
    for j in range(int(m)):
        sum += arr[i][j]
    if sum >= maxi:
        maxi = sum
for j in range(int(m)):
    sum = 0
    for i in range(int(n)):
        sum += arr[i][j]
    if sum >= maxi:
        maxi = sum
print(maxi)