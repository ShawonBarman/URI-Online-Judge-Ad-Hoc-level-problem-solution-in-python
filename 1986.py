n = int(input())
arr = list(map(str, input().split()))[:n]
ans = ""
for i in range(len(arr)):
    ans += chr(int(arr[i], 16))
print(ans)