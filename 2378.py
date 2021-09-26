n, c = map(int, input().split())
ans = "N"
total = 0
for i in range(n):
    s, e = map(int, input().split())
    total = total - s + e
    if total > c:
        ans = "S"
print(ans)