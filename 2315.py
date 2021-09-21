days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a, b = map(int, input().split())
x, y = map(int, input().split())
total_days = 0
if b-y == 0:
    total_days = x - a
elif b-y == 1:
    total_days = (days[b-1] - a)+x
else:
    total_days = days[b - 1] - a
    for i in range(b,y-1):
        total_days += days[i]
    total_days += x

print(total_days)