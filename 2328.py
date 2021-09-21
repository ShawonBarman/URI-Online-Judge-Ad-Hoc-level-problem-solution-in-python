n = int(input())
arr = list(map(int, input().split()))[:n]
addition = sum(arr)
print(addition-n)