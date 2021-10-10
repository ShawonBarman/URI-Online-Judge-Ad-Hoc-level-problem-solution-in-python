n = int(input())
grades = list(map(int, input().split()))[:n]
mi = -999999
for x in grades:
    total = grades.count(x)
    if total > mi:
        mi = total
new_arr = []
for x in grades:
    total = grades.count(x)
    if total == mi:
        new_arr.append(x)
print(max(new_arr))