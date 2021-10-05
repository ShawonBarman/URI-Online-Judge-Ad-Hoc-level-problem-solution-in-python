v, t = map(int, input().split())
ai = list(map(int, input().split()))[:t]
for x in ai:
    v += x
    if v < 0:
        v = 0
    elif v > 100:
        v = 100
print(v)