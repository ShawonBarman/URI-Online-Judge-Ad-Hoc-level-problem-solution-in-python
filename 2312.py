def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y
def bubble_sort(countries, g, s, b):
    i = 0
    while i < len(countries)-1:
        k = 0
        while k < len(countries)-i-1:
            if g[k+1] > g[k]:
                g[k], g[k+1] = swap(g[k], g[k+1])
                s[k], s[k + 1] = swap(s[k], s[k + 1])
                b[k], b[k + 1] = swap(b[k], b[k + 1])
                countries[k], countries[k + 1] = swap(countries[k], countries[k + 1])
            if g[k + 1] == g[k]:
                if s[k+1] > s[k]:
                    g[k], g[k + 1] = swap(g[k], g[k + 1])
                    s[k], s[k + 1] = swap(s[k], s[k + 1])
                    b[k], b[k + 1] = swap(b[k], b[k + 1])
                    countries[k], countries[k + 1] = swap(countries[k], countries[k + 1])
                if s[k+1] == s[k]:
                    if b[k+1] > b[k]:
                        g[k], g[k + 1] = swap(g[k], g[k + 1])
                        s[k], s[k + 1] = swap(s[k], s[k + 1])
                        b[k], b[k + 1] = swap(b[k], b[k + 1])
                        countries[k], countries[k + 1] = swap(countries[k], countries[k + 1])
                    if b[k+1] == b[k]:
                        if countries[k+1] > countries[k]:
                            g[k], g[k + 1] = swap(g[k], g[k + 1])
                            s[k], s[k + 1] = swap(s[k], s[k + 1])
                            b[k], b[k + 1] = swap(b[k], b[k + 1])
                            countries[k], countries[k + 1] = swap(countries[k], countries[k + 1])
            k += 1
        i += 1

n = int(input())
countries = []
g = []
s =[]
b = []
while n != 0:
    n -= 1
    x, y, z, w = input().split()
    countries.append(x)
    g.append(int(y))
    s.append(int(z))
    b.append(int(w))
bubble_sort(countries, g, s, b)
for i in range(len(countries)):
    print(f"{countries[i]} {g[i]} {s[i]} {b[i]}")