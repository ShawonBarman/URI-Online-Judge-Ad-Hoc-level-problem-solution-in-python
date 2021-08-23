while True:
    try:
        n = int(input())
        while n != 0:
            n -= 1
            s = int(input())
            array1 = list(map(int, input().split()))[:s]
            array2 = list(input())
            count = 0
            for i in range(s):
                if array2[i] == "J" and array1[i] > 2:
                    count += 1
                elif array2[i] == "S" and (array1[i] == 1 or array1[i] == 2):
                    count += 1
            print(count)
    except EOFError:
        break