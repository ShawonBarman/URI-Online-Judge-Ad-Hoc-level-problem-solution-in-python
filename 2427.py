l = int(input())
count = 0
while l >= 2:
    l = l/2
    count += 2
print(2**count)