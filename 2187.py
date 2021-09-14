notes = [50, 10, 5, 1]
count = 1
while True:
    v = int(input())
    if v == 0:
        break
    arr = [0]*4
    while v != 0:
        for i in range(len(notes)):
            if v - notes[i] >= 0:
                v -= notes[i]
                arr[i] += 1
                break
    print(f"Teste {count}")
    count += 1
    for i in range(len(arr)-1):
        print(arr[i], end=" ")
    print(arr[len(arr)-1])
    print()