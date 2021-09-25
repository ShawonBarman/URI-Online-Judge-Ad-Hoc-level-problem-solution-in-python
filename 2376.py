teams = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]

arr = []
for i in range(0,15,2):
    m, n = map(int, input().split())
    if m > n:
        arr.append(teams[i])
    else:
        arr.append(teams[i+1])

arr2 = []
for i in range(0,7,2):
    m, n = map(int, input().split())
    if m > n:
        arr2.append(arr[i])
    else:
        arr2.append(arr[i + 1])

arr3 = []
for i in range(0,3,2):
    m, n = map(int, input().split())
    if m > n:
        arr3.append(arr2[i])
    else:
        arr3.append(arr2[i + 1])

m, n = map(int, input().split())
if m > n:
    print(arr3[0])
else:
    print(arr3[1])