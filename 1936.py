arr = [0,1,2,6,24,120,720,5040,40320,362880]
n = int(input())
count = 0
for i in range(len(arr)):
    if n < arr[i]:
        count = i
        break
ans = 0
tmp = n
x = count
while tmp != 0:
    x -= 1
    if tmp - arr[x] >= 0:
        tmp -= arr[x]
        x = count
        ans += 1
print(ans)
