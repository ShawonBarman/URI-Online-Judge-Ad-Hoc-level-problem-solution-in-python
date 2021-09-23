n = int(input())
x_arr = []
y_arr = []
for i in range(n):
    x, y = input().split()
    x_arr.append(int(x))
    y_arr.append(int(y))
x_max = max(x_arr)
y_max = max(y_arr)
arr = []
for i in range(x_max+1):
    arr.append([0]*(y_max+1))
for i in range(n):
    arr[x_arr[i]][y_arr[i]] += 1
ans = 0
for i in range(x_max+1):
    for j in range(y_max+1):
        if arr[i][j] > 1:
            ans = 1
print(ans)