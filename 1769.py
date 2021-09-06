while True:
    try:
        cpf_number = input()
        b1 = 0
        b2 = 0
        a = 1
        b = 9
        for x in cpf_number:
            if x == "-":
                break
            elif x.isdigit():
                b1 += int(x)*a
                a += 1
                b2 += int(x)*b
                b -= 1
        b1 = (b1 % 11)%10
        b2 = (b2 % 11)%10
        if b1 == int(cpf_number[-2]) and b2 == int(cpf_number[-1]):
            print("CPF valido")
        else:
            print("CPF invalido")
    except EOFError:
        break