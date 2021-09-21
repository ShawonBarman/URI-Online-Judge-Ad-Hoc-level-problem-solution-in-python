n = int(input())
arr = list(map(int, input().split()))[:(n-1)]
missing_value = 0
for i in range(1,n+1):
    if i not in arr:
        missing_value = i
print(missing_value)