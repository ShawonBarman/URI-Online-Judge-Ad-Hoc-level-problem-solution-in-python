n = int(input())
add_sign = 0
minus_sign = 0
array = []
for i in range(n):
    sign, name = input().split()
    if sign == '+':
        add_sign += 1
    elif sign == '-':
        minus_sign += 1
    array.append(name)
array.sort()
for name in array:
    print(name)
print(f"Se comportaram: {add_sign} | Nao se comportaram: {minus_sign}")