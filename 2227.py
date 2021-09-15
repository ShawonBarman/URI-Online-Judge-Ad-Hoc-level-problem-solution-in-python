count = 1
while True:
    a, v = map(int, input().split())
    if a == v == 0:
        break
    arr = [0] * a
    for i in range(v):
        x, y = input().split()
        arr[int(x)-1] += 1
        arr[int(y)-1] += 1
    maxi = max(arr)
    media = []
    for i in range(len(arr)):
        if arr[i] == maxi:
            media.append(str(i+1))
    print(f"Teste {count}")
    count += 1
    print(' '.join(media), '')
    print()