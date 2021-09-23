n = int(input())
p, sign, q = input().split()
ans = 0
if sign == "+":
    ans = int(p) + int(q)
elif sign == "*":
    ans = int(p) * int(q)
if ans <= n:
    print("OK")
else:
    print("OVERFLOW")