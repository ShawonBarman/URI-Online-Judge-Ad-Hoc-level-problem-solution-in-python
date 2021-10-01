n = int(input())
v = list(map(int, input().split()))[:n]
largest_sequence = 1
count = 1
for i in range(1, n):
    if v[i] == v[i - 1]:
        count += 1
    else:
        if count > largest_sequence:
            largest_sequence = count
        count = 1

if count > largest_sequence:
    largest_sequence = count
print(largest_sequence)