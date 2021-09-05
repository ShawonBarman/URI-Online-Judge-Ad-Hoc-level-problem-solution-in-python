while True:
    inp = input()
    if inp == "0+0=0":
        print("True")
        break
    a, anx = inp.split("+")
    b, c = anx.split("=")
    a = int(a[::-1])
    b = int(b[::-1])
    c = int(c[::-1])
    if a+b == c:
        print("True")
    else:
        print("False")