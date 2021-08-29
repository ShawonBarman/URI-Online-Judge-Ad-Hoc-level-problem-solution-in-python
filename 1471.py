while True:
    try:
        n, r = map(int, input().split())
        n = [x for x in range(1,n+1)]
        returned_volunteer = list(map(int, input().split()))[:r]
        arr = list()
        for i in n:
            if i not in returned_volunteer:
                arr.append(i)
        if len(arr) == 0:
            print("*")
        else:
            for i in range(len(arr)):
                print(arr[i], end=" ")
            print()
    except EOFError:
        break