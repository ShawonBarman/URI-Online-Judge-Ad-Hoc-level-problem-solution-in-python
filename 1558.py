from math import sqrt
arr = [0] * 11001
length = int(sqrt(11000))
for i in range(length+1):
    for j in range(i, length+1):
        if(i * i + j * j) > 11000:
            break
        arr[i*i + j*j] = 1

while True:
    try:
        n = int(input())
        if n < 0:
            print('NO')
        else:
            if arr[n]:
                print('YES')
            else:
                print('NO')

    except EOFError:
        break