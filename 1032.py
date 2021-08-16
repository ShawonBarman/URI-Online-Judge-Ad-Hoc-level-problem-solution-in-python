from collections import deque

def gen_primeNumber():
    pm = [2, 3, 5, 7]
    i = 10
    while len(pm) != 3501:
        for j in pm:
            if i % j == 0:
                break
            if j == pm[len(pm) - 1]:
                pm.append(i)
        i += 1
    return pm

primes = gen_primeNumber()

while True:
    n = int(input())
    if n == 0:
        break
    n = [x for x in range(1, n+1)]
    d = deque(n)
    i = 0
    while len(d) > 1:
        d.rotate(-primes[i])
        d.pop()
        i += 1
    print(d.pop())