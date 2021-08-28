direction = ['N', 'L', 'S', 'O']
while True:
    n = int(input())
    if n == 0:
        break
    initial = 0
    x = input()
    if len(x) == n:
        for i in x:
            if i == 'D':
                initial += 1
            elif i == 'E':
                initial -= 1
            if initial == len(direction) or initial == -len(direction):
                initial = 0

    print(direction[initial])