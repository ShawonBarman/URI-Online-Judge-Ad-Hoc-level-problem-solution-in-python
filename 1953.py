while True:
    try:
        n = int(input())
        epr = 0
        ehd = 0
        intrusos = 0
        while n != 0:
            n -= 1
            inp = input().split()
            if inp[1] == 'EPR':
                epr += 1
            elif inp[1] == 'EHD':
                ehd += 1
            else:
                intrusos += 1
        print(f"EPR: {epr}")
        print(f"EHD: {ehd}")
        print(f"INTRUSOS: {intrusos}")
    except EOFError:
        break