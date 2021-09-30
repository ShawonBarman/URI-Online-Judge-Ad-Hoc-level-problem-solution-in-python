a, b, c = map(int, input().split())
h, l = map(int, input().split())
if a <= h and b <= l:
    print("S")
elif a <= h and c <= l:
    print("S")
elif b <= h and a <= l:
    print("S")
elif b <= h and c <= l:
    print("S")
elif c <= h and a <= l:
    print("S")
elif c <= h and b <= l:
    print("S")
else:
    print("N")