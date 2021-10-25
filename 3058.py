n = int(input())
min_cost = 999999999
while n != 0:
    n -= 1
    p, g = input().split()
    min_cost = min(min_cost, float(p)*1000/int(g))
print("{0:.2f}".format(min_cost))