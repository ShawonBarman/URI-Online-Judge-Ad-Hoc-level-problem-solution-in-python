n = int(input())
time = []
total = 0
for i in range(n):
    t = int(input())
    time.append(t)
for i in range(len(time)-1,0,-1):
    total += (time[i]-time[i-1])
print(total+10)

# 45% wrong answer