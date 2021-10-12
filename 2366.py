n, m = map(int, input().split())
arr = list(map(int, input().split()))[:n]
flag = True
for i in range(n-1):
    if arr[i+1]-arr[i] > m:
        flag = False
if flag and ((42195-arr[len(arr)-1]) <= m):
    print("S")
else:
    print("N")