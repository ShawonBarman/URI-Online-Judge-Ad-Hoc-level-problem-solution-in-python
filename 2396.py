n, m = input().split()
arr = []
for i in range(int(n)):
    num = list(map(int, input().split()))[:int(m)]
    arr.append(sum(num))
for i in range(3):
    x = arr.index(min(arr))
    print(x+1)
    arr[x] = 9999999999