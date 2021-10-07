word = input()
text = input().split()
total = 0
for wd in text:
    if word in wd:
        total += 1
print("{:.1f}".format(total/(len(text)/100)))