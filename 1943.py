position = [1, 3, 5, 10, 25, 50, 100]
k = int(input())
for pos in position:
    if k <= pos:
        k = pos
        break
print(f"Top {k}")