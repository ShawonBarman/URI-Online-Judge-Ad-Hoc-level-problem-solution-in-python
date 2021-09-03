t = int(input())
while t:
    t -= 1
    i = int(input())
    binary_value = bin(i)
    print(binary_value.count('1'))