n = int(input())
while n:
    n -= 1
    a, b, c, d = map(int,  input().split())
    growing_rate = (d-b)/(c-a)
    # print(growing_rate)
    growing_rate = str('%.4f' % growing_rate).replace('.', ',')
    # print(growing_rate)
    growing_rate = growing_rate[:len(growing_rate) - 2]
    print(growing_rate)