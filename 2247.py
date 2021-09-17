count = 1
while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for i in range(n):
        j, z = map(int, input().split())
        arr.append(j-z)
    for i in range(1,len(arr)):
        arr[i] = arr[i] + arr[i-1]
    print(f"Teste {count}")
    count += 1
    for x in arr:
        print(x)
    print()