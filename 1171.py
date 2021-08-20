n = int(input())
arr = []
while n != 0:
    n -= 1
    arr.append(int(input()))
another_arr= list(set(arr))
another_arr.sort()
for i in range(len(another_arr)):
    print(f"{another_arr[i]} aparece {arr.count(another_arr[i])} vez(es)")