arr = []
for i in range(2,1001):
    flag = 0
    for j in range(2,i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        arr.append(i)
# print(arr)
n, m = map(int, input().split())
p1 = 0
p2 = 0
for x in arr:
    if n >= x:
        p1 = x
    if m >= x:
        p2 = x
# print(p1, p2)
print(p1 * p2)