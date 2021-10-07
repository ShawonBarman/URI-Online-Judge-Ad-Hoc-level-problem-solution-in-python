arr = list(map(int, input().split()))[:5]
inc = 0
dec = 0
for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        inc += 1
    elif arr[i] < arr[i-1]:
        dec += 1
if inc == 4:
    print("C")
elif dec == 4:
    print("D")
else:
    print("N")