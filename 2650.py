n, w = map(int, input().split())
for i in range(n):
    inp = input().split()
    h = int(inp[-1])
    name = inp[0]
    for j in range(1, len(inp)-1):
        name += " " + inp[j]
    if h > w:
        print(name)