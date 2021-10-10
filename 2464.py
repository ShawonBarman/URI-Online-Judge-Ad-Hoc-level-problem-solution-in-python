alphabet = "abcdefghijklmnopqrstuvwxyz"
first_text = input()
second_text = input()
ans = ""
for i in range(len(second_text)):
    ans += alphabet[first_text.index(second_text[i])]
print(ans)