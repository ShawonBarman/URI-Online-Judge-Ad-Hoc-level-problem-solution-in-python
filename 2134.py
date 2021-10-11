count = 1
while True:
    try:
        n = int(input())
        temp = 9999
        nm = ""
        for i in range(n):
            name, solved = input().split()
            if int(solved) < temp:
                temp = int(solved)
                nm = name
        print(f"Instancia {count}")
        print(nm)
        count += 1
    except EOFError:
        break

#Wrong answer (5%)