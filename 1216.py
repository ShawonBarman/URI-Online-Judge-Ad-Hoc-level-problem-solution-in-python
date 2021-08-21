sum = 0
count = 0
while True:
    try:
        name = input()
        distance = int(input())
        sum += distance
        count += 1
    except EOFError:
        break

print("{:.1f}".format(sum/count))