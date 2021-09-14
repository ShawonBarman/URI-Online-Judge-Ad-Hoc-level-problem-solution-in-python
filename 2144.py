count = 0
sum = 0
while True:
    w1, w2, r = map(int, input().split())
    if w1 == 0 and w2 == 0 and r == 0:
        break
    m = ((w1 * (1 + r/30))+(w2 * (1 + r/30)))/2
    sum += m
    count += 1
    if m >= 1 and m < 13:
        print("Nao vai da nao")
    elif m >= 13 and m < 14:
        print("E 13")
    elif m >= 14 and m < 40:
        print("Bora, hora do show! BIIR!")
    elif m >= 40 and m <= 60:
        print("Ta saindo da jaula o monstro!")
    elif m > 60:
        print("AQUI E BODYBUILDER!!")

avg = sum/count
if avg > 40:
    print()
    print("Aqui nois constroi fibra rapaz!")
    print("Nao e agua com musculo!")