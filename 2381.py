n, k = map(int,input().split())
names = []
for i in range(n):
    names.append(input())
names.sort()
print(names[k-1])