n, m = map(int, input().split())
temp = 0
total = 0
winner = 0
for i in range(n):
    laptime = list(map(int, input().split()))[:m]
    total = sum(laptime)
    if i == 0:
        temp = total
        winner = i
    elif i > 0 and total < temp:
        temp = total
        winner = i
print(winner+1)