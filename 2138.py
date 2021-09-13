while True:
    try:
        n = input()
        arr = []
        for x in n:
            if int(x) not in arr:
                arr.append(int(x))
        arr.sort()
        most_frequent_digit = 0
        max_count = 0
        for x in arr:
            if n.count(str(x)) >= max_count:
                max_count = n.count(str(x))
                most_frequent_digit = x
        print(most_frequent_digit)
    except EOFError:
        break