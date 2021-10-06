def binary_search(number_of_houses, value):
    high = len(number_of_houses)
    low = 1
    while low <= high:
        mid = int((low+high)/2)
        if value < number_of_houses[mid]:
            high = mid-1
        elif value > number_of_houses[mid]:
            low = mid + 1
        else:
            return mid
    return 0
n, m = input().split()
number_of_houses = list(map(int, input().split()))[:int(n)]
number_of_orders = list(map(int, input().split()))[:int(m)]
ans = 0
temp = 1
for x in number_of_orders:
    aux = binary_search(number_of_houses, x)
    ans += abs(aux-temp)
    temp = aux
print(ans)

# Wrong answer (10%)