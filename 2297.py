count = 1
while True:
    r = int(input())
    if r == 0:
        break
    aldo = 0
    beto = 0
    for i in range(r):
        a, b = input().split()
        aldo += int(a)
        beto += int(b)
    print(f"Teste {count}")
    count += 1
    if aldo > beto:
        print("Aldo")
    else:
        print("Beto")
    print()