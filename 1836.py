import math

t = int(input())
for i in range(1,t+1):
    p, l = input().split()
    print(f"Caso #{i}: {p} nivel {int(l)}")
    bs, iv, ev = map(int, input().split())
    hp = (((iv + bs + math.sqrt(ev)/8 + 50) * int(l))/50)+10
    print(f"HP: {int(hp)}")
    bs, iv, ev = map(int, input().split())
    at = (((iv + bs + math.sqrt(ev) / 8) * int(l)) / 50) + 5
    print(f"AT: {int(at)}")
    bs, iv, ev = map(int, input().split())
    df = (((iv + bs + math.sqrt(ev) / 8) * int(l)) / 50) + 5
    print(f"DF: {int(df)}")
    bs, iv, ev = map(int, input().split())
    sp = (((iv + bs + math.sqrt(ev) / 8) * int(l)) / 50) + 5
    print(f"SP: {int(sp)}")