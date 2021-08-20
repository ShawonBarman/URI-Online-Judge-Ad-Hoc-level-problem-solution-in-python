keyboard = '`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./'
while True:
    try:
        text = input()
        ans = ''
        for letter in text:
            if letter == ' ':
                ans += letter
            else:
                ans += keyboard[keyboard.index(letter)-1]
        print(ans)
    except EOFError:
        break