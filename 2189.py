count = 1
while True:
    n = int(input())
    if n == 0:
        break
    numbers = list(map(int, input().split()))[:n]
    for i in range(len(numbers)):
        if numbers[i] == i+1:
            print(f"Teste {count}")
            print(numbers[i])
            print()
            count += 1