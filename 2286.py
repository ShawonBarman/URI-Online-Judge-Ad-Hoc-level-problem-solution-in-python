count = 1
while True:
    n = int(input())
    if n == 0:
        break
    a_name = input()
    b_name = input()
    print(f"Teste {count}")
    count += 1
    for i in range(n):
        a, b = map(int, input().split())
        if a%2 == 0 and b%2 == 0:
            print(a_name)
        elif a%2 == 1 and b%2 == 1:
            print(a_name)
        else:
            print(b_name)
    print()