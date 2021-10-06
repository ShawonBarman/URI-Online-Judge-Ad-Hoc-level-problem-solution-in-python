msg = input()
count = 0
ans = ""
while count < len(msg)-1:
    if msg[count].lower() == 'p':
        count += 1
        ans += msg[count]
        count += 1
    else:
        ans += msg[count]
        count += 1
print(ans)