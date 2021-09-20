l, n = input().split()
dic = {
    "D" : int(l),
    "E" : int(l),
    "F" : int(l)
}
for i in range(int(n)):
    op, value = input().split()
    x, y, z = "", "", ""
    if len(op) == 2:
        x, y = op[0], op[1]
    elif len(op) == 3:
        x, y, z = op[0], op[1], op[2]

    if x == "C":
        dic[y] -= int(value)
    elif y == "C":
        dic[x] -= int(value)
    elif x == "V":
        dic[y] += int(value)
    elif y == "V":
        dic[x] += int(value)
    elif x == "A":
        dic[y] += int(value)
        dic[z] -= int(value)
print(f"{dic['D']} {dic['E']} {dic['F']}")