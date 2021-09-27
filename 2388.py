n = int(input())
sum = 0
for i in range(n):
    t, v = input().split()
    sum += int(t)*int(v)
print(sum)