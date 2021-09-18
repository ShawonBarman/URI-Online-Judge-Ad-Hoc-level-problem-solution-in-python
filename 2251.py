arr = list()
arr.append(0)
for i in range(1,31):
    arr.append(pow(2,i)-1)
count = 1
while True:
    n = int(input())
    if n == 0:
        break
    print(f"Teste {count}")
    count += 1
    print(arr[n])
    print()