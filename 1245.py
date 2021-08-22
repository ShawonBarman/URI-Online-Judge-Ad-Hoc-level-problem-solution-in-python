while True:
    try:
        n = int(input())
        D = list()
        E = list()
        for i in range(n):
            m, l = input().split()
            if l == 'D':
                D.append(m)
            else:
                E.append(m)
        # print(boots_list)
        count = 0
        for x in D:
            if x in E:
                count += 1
                E.remove(x)
        print(count)
    except EOFError:
        break