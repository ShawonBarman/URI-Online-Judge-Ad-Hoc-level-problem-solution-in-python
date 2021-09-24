n = int(input())
ans = 7
if n > 100:
    ans += (n-100)*5 + 160
elif n > 30:
    ans += (n-30)*2 + 20
elif n > 10:
    ans += (n-10) * 1
print(ans)