while True:
    try:
        a, b = input().split()
        if a == '0' and b == '0':
            break
        x = list(map(int, input().split()))[:int(a)]
        y = list(map(int,input().split()))[:int(b)]
        x = set(x)
        y = set(y)
        arr = []
        if len(x) < len(y):
            for i in x:
                if i not in y:
                    arr.append(i)
        else:
            for i in y:
                if i not in x:
                    arr.append(i)

        print(len(arr))
    except EOFError:
        break