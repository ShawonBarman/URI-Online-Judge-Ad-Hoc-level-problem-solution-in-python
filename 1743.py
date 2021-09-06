flag = "Y"
x = list(map(int, input().split()))[:5]
y = list(map(int, input().split()))[:5]
for i in range(5):
    if (x[i] == 1 and y[i] == 1) or (x[i] == 0 and y[i] == 0):
        flag = "N"
print(flag)