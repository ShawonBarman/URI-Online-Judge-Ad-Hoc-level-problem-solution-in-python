count = 1
while True:
    n = int(input())
    if n == 0:
        break
    dic = dict()
    for i in range(n):
        c, m = input().split()
        dic.update({int(c):int(m)})
    arr = []
    maxi = max(dic.values())
    for id, avg in dic.items():
        if maxi == avg:
            arr.append(str(id))
    print(f"Turma {count}")
    count += 1
    print(' '.join(arr), '')
    print()