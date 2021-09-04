t = int(input())
while t != 0:
    t -= 1
    n = int(input())
    numbers = list(map(int, input().split()))[:n]
    numbers = set(numbers)
    print(len(numbers))