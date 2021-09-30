n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr = list(set(arr))
print(len(arr))