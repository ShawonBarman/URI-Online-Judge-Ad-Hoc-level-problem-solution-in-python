arr = []
arr.append(0)
arr.append(1)
i = 0
while len(arr) != 61:
    if i == 0:
        arr.append(2)
    else:
        x = str(arr[i])
        x = x[::-1]
        y = str(arr[i+1])
        y = y[::-1]
        arr.append(int(x)+int(y))
    i += 1
while True:
    try:
        x = int(input())
        print(arr[x])
    except EOFError:
        break

