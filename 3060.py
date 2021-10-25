v = int(input())
p = int(input())
if v%p==0:
    x = int(v/p)
    for i in range(p):
        print(x)
else:
    x = v%p
    y = int(v/p)
    for i in range(x):
        print(y+1)
    for i in range(p-x):
        print(y)