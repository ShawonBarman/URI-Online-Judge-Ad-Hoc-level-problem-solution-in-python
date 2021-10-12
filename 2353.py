n = int(input())
if n == 2:
    print(2)
else:
    if n%2 == 0:
        n -= 1
    for i in range(n, 1, -2):
        flag = True
        size = int(pow(i,0.5))
        for j in range(3, size+1):
            if i % j == 0:
                flag = False
                break
        if flag:
            print(i)
            break