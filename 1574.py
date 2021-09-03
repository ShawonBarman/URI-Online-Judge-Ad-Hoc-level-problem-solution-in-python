t = int(input())
while t != 0:
    t -= 1
    n = int(input())
    arr = list()
    for i in range(n):
        inp = input()
        if inp == "LEFT":
            arr.append("LEFT")
        elif inp == "RIGHT":
            arr.append("RIGHT")
        else:
            x = inp.split()
            if arr[int(x[2])-1] == "LEFT":
                arr.append("LEFT")
            elif arr[int(x[2])-1] == "RIGHT":
                arr.append("RIGHT")
    sum = 0
    for i in arr:
        if i == "LEFT":
            sum -= 1
        elif i == "RIGHT":
            sum += 1
    print(sum)