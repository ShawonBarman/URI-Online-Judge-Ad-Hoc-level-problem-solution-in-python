n = int(input())
flag = True
if n == 1 or n == 2:
    flag = True
if n % 2 == 0:
    flag = False
else:
    i = 3
    while i*i <= n:
        if n % i == 0:
            flag = False
            break
        i += 2
if flag == True:
    print("N")
else:
    print("S")