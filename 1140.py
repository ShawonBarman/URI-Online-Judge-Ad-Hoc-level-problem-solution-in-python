sun = True
while sun:
    try:
        word = input()
        # print(word)
        if word == "*":
            sun = False
        else:
            word = (word.lower()).split()
            letter = word[0][0].lower()
            flag = 1
            for wd in word:
                if (wd.lower()).startswith(letter):
                    continue
                else:
                    flag = 0
                    break

            if flag == 1:
                print("Y")
            else:
                print("N")
    except EOFError:
        break