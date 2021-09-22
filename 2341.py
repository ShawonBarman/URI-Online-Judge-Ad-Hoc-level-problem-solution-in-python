n, k = map(int, input().split())
xi = list(map(int, input().split()))[:n]
arr = [0]*k
for x in xi:
    arr[x-1] += 1
mini = 999999999
for i in range(len(arr)):
    mini = min(mini, arr[i])
print(mini)