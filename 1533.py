while True:
    n = int(input())
    if n == 0:
        break
    array = list(map(int, input().split()))[:n]
    copy_array = []
    copy_array.extend(array)
    copy_array.sort()
    pos = copy_array[n-2]
    for i in range(n):
        if array[i] == pos:
            print(i+1)
            break