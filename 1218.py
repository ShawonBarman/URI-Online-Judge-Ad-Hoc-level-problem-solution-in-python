x = 0
while True:
    try:
        x += 1
        n = input()
        shoes_pair = list(map(str, input().split()))
        count = 0
        male = 0
        female = 0
        for i in range(0, len(shoes_pair), 2):
            if shoes_pair[i] == n:
                count += 1
                if shoes_pair[i + 1] == "M":
                    male += 1
                elif shoes_pair[i + 1] == "F":
                    female += 1
        if x > 1:
            print()
        print(f"Caso {x}:")
        print(f"Pares Iguais: {count}")
        print(f"F: {female}")
        print(f"M: {male}")
    except EOFError:
        break