n = int(input())
kg = []
spent = 0
count = 0
while n != 0:
    n -= 1
    v = float(input())
    spent += v
    fruits = input().split()
    kg.append(len(fruits))
    count += 1
for i in range(len(kg)):
    print(f"day {i+1}: {kg[i]} kg")
print("{:.2f} kg by day".format(sum(kg)/len(kg)))
print("R$ {:.2f} by day".format(spent/count))