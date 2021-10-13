first_numbers = list(map(int, input().split()))[:6]
second_numbers = list(map(int, input().split()))[:6]
count = 0
for x in first_numbers:
    if x in second_numbers:
        count += 1
if count < 3:
    print("azar")
elif count == 3:
    print("terno")
elif count == 4:
    print("quadra")
elif count == 5:
    print("quina")
elif count == 6:
    print("sena")