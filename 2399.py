n = int(input())
arr = [0, 0, 0]
ans_arr = []
for i in range(n+1):
    if i < n:
        x = int(i%3)
        arr[x] = int(input())
    else:
        x = int(i % 3)
        arr[x] = 0
    if i > 0:
        ans_arr.append(sum(arr))
for x in ans_arr:
    print(x)