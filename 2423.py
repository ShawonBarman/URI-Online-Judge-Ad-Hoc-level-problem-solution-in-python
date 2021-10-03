a, b, c = map(int, input().split())
count = 0
while a >= 2 and b >= 3 and c >= 5:
    a -= 2
    b -= 3
    c -= 5
    count += 1
print(count)