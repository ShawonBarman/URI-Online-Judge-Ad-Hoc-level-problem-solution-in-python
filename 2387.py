n = int(input())
x_arr = []
y_arr = []
for i in range(n):
    x, y = input().split()
    x_arr.append(int(x))
    y_arr.append(int(y))
y_arr.sort()
j = 0
count = 1
for i in range(1, n):
    if x_arr[i] >= y_arr[j]:
        count += 1
        j = i
print(count)

#35% wrong answer