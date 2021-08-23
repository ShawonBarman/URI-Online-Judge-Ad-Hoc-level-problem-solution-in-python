while True:
    num = int(input())
    if num == 0:
        break
    arrays = list(map(int, input().split()))
    count = arrays.count(1)
    m = 0
    for i in range(num):
        if count * i > num:
            break
        else:
            m = i
    print(m)

# Wrong answer (35%)