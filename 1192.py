n = int(input())
while n != 0:
    n -= 1
    word = input()
    first_digit = int(word[2])
    second_digit = int(word[0])
    character = word[1]
    if character.isupper() and first_digit != second_digit:
        print(first_digit - second_digit)
    elif character.islower() and first_digit != second_digit:
        print(first_digit + second_digit)
    elif first_digit == second_digit:
        print(first_digit * second_digit)