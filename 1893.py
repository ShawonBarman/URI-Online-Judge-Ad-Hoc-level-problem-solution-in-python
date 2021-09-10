first_number, second_number = map(int, input().split())
if second_number >= 0 and second_number <= 2:
    print('nova')
elif second_number <= 100 and second_number >= 97:
    print('cheia')
elif second_number > first_number :
    print('crescente')
else:
    print('minguante')