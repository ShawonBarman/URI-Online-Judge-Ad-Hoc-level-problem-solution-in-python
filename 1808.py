s = input()
arr = [0] * len(s)
i = 0
j = 0
while s[i] != "":
    while True:
        if s[i] == '0' or s[i] == '':
            break
        arr[j+1] = int(s[i+1])-48
    if s[i] == '0':
        arr[j-1] *= 10
    if s[i] == "":
        i += 1
        j += 1
media = sum(arr)
print("{:.2f}".format(media/j))