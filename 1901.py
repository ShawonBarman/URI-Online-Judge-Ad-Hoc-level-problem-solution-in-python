n = int(input())
arr = []
for i in range(n):
    another_arr = list(map(int, input().split()))[:n]
    arr.append(another_arr)
ans = []
for x in range(n*2):
    i, j = map(int, input().split())
    if arr[i-1][j-1] in ans:
        continue
    else:
        ans.append(arr[i-1][j-1])
print(len(ans))