a, b, c = map(int, input().split())
if (a > b and a < c) or (a < b and a > c):
    print(a)
elif (b > a and b < c) or (b < a and b > c):
    print(b)
else:
    print(c)