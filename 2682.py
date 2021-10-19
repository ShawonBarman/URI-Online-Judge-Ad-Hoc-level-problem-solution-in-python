ans = 0
tmp = 0
while True:
    try:
        n = int(input())
        if tmp > n and ans == 0:
            ans = tmp + 1
        tmp = n

    except EOFError:
        break

if ans == 0:
    ans = tmp + 1
print(ans)