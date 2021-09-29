import math
inp = list(map(int, input().split()))
inp.sort()
x, y, z = inp[0], inp[1], inp[2]
if x+y<=z or x+z<=y or y+z<=z:
    print("n")
else:
    if math.sqrt(x*x + y*y) > z:
        print("a")
    elif math.sqrt(x*x + y*y) == float(z):
        print("r")
    else:
        print("o")