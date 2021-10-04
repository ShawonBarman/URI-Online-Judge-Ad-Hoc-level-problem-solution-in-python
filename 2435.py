n1, d1, v1 = map(int, input().split())
avg1 = d1 / v1
n2, d2, v2 = map(int, input().split())
avg2 = d2 / v2
if avg1 < avg2:
    print(n1)
else:
    print(n2)