n, s = map(int, input().split())
total = 1001
for i in range(n):
    s += int(input())
    if s < total:
        total = s
print(total)