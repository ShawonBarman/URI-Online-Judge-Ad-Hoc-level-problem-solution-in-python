while True:
    n, k = map(int, input().split())
    if n==0 and k==0:
        break
    arr = input().split()
    low = 1
    high = n
    while low < high:
        mid = int(low + (high-low)/2)
        if mid*(mid+1)/2 >= k:
            high = mid
        else:
            low = mid+1
    print(arr[int(k-((low-1)*low/2))-1])