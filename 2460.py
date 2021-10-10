n = int(input())
n_arr = list(map(int, input().split()))[:n]
m = int(input())
m_arr = list(map(int, input().split()))[:m]
for x in m_arr:
    n_arr.remove(x)
for i in range(len(n_arr)-1):
    print(n_arr[i], end=" ")
print(n_arr[len(n_arr)-1])