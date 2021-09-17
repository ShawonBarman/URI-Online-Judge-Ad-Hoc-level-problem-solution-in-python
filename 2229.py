count = 1
while True:
    n = int(input())
    if n == -1:
        break
    ans = 0
    if n == 0:
        ans = 4
    elif n == 1:
        ans = 9
    else:
        ans = (1 + pow(2, n))*(1 + pow(2, n))
    print(f"Teste {count}")
    count += 1
    print(ans)
    print()