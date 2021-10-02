n = list(map(float, input().split()))[:5]
n.sort()
print("{:.1f}".format(n[1]+n[2]+n[3]))