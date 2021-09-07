while True:
    try:
        number = input()
        b1 = 0
        b2 = 0
        a = 1
        b = 9
        cpf_number = ""
        for x in number:
            b1 += int(x)*a
            a += 1
            b2 += int(x)*b
            b -= 1
            cpf_number += x
            if a == 4 or a == 7:
                cpf_number += "."
        b1 = (b1 % 11)%10
        b2 = (b2 % 11)%10
        cpf_number += "-"+str(b1)+str(b2)
        print(cpf_number)
    except EOFError:
        break