n = int(input())
while n != 0:
    n -= 1
    qt, s = input().split()
    array = list(map(int, input().split()))[:int(qt)]
    s = int(s)
    diff = 9999999
    pos = 0
    count = 0
    temp = 0
    for x in array:
        temp = s - x
        count += 1
        if temp < 0:
            temp = -temp
        if temp < diff:
            diff = temp
            pos = count
    print(pos)