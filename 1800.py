q, e = input().split()
si = list(map(int, input().split()))[:int(e)]
for i in range(int(q)):
    ci = int(input())
    if ci in si:
        print(0)
    else:
        print(1)
        si.append(ci)