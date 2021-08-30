while True:
    n = int(input())
    if n == 0:
        break
    galaxy_name = ""
    year = 999999
    for i in range(n):
        name, a, t = input().split()
        if int(a) - int(t) < year:
            year = int(a) - int(t)
            galaxy_name = name
    print(galaxy_name)