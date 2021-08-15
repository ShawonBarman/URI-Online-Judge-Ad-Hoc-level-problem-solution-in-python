def func(n, k):
    result = 0
    for i in range(2, n+1):
        result = (result + k) % i
    return result + 1

nc = int(input())

for i in range(1, nc+1):
    n, k = map(int, input().split())
    print(f"Case {i}: {func(n, k)}")

# Anather Easiest way
# from collections import deque
#
# nc = int(input())
#
# for i in range(1, nc+1):
#     n, k = map(int, input().split())
#     n = [x for x in range(1, n+1)]
#     d = deque(n)
#     while len(d) > 1:
#         d.rotate(-k)
#         d.pop()
#     print(f"Case {i}: {d.pop()}")