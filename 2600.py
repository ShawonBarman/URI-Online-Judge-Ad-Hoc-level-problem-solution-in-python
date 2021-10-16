numbers = [1, 2, 3, 4, 5, 6]
n = int(input())
while n != 0:
    n -= 1
    array = []
    array.append(int(input()))
    x = list(map(int, input().split()))[:4]
    array.extend(x)
    array.append(int(input()))
    sorted_array = sorted(array)
    if (sorted_array != numbers) or (array[0]+array[5] != 7) or (array[1]+array[3] != 7) or (array[2]+array[4] != 7):
        print("NAO")
    else:
        print("SIM")