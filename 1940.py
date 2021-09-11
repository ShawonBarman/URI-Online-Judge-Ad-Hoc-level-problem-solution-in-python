j, r = map(int, input().split())
players = [0] * j
v = list(map(int, input().split()))[:j * r]
for i in range(len(v)):
    players[i%j] += v[i]
maxi = players[0]
pos = 0
for i in range(len(players)):
    if maxi <= players[i]:
        maxi = players[i]
        pos = i
print(pos+1)