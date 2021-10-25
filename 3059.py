n, l, f = map(int, input().split())
array = list(map(int, input().split()))[:n]
count = 0
for i in range(n):
    for j in range(i+1,n):
        if array[i] != array[j]:
            if array[i]+array[j] >= l and array[i]+array[j] <= f:
                count += 1
print(count)