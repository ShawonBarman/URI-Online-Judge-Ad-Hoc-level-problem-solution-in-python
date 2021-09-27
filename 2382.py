import math
l, a, p, r = map(int, input().split())
dia = math.sqrt((l*l)+(a*a)+(p*p))
if dia <= 2*r:
    print("S")
else:
    print("N")