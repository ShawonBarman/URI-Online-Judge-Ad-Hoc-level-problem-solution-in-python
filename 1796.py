q = int(input())
v = list(map(int, input().split()))[:q]
ok = v.count(0)
not_ok = v.count(1)
if ok > not_ok:
    print("Y")
else:
    print("N")