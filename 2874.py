while True:
    try:
        n = int(input())
        ans = ""
        while n != 0:
            n -= 1
            b = input()
            dec_value = int(b, 2) #convert binary to decimal
            ans += chr(dec_value) #convert ascii to character
        print(ans)
    except EOFError:
        break