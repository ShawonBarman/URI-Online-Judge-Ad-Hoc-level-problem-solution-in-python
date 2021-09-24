n, m = input().split()
arr = []
for i in range(1, int(n)+1):
    arr.append(i)
for i in range(int(m)):
    op, x, y = input().split()
    x = int(x)
    y = int(y)
    if op == 'I':
        while x < y:
            temp = arr[x-1]
            arr[x-1] = arr[y-1]
            arr[y-1] = temp
            x += 1
            y -= 1
    elif op == 'S':
        sum = 0
        for i in range(x,y+1):
            sum += arr[i-1]
        print(sum)