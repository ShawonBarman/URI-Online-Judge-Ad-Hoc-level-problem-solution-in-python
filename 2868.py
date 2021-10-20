c = int(input())
while c != 0:
    c -= 1
    num1, sign1, num2, sign2, ans = input().split()
    correct_ans = 0
    if sign1 == "+":
        correct_ans = int(num1) + int(num2)
    elif sign1 == "-":
        correct_ans = int(num1) - int(num2)
    else:
        correct_ans = int(num1) * int(num2)
    answer = 'r' * abs(correct_ans - int(ans))
    print(f"E{answer}ou!")