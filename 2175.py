o, b, l = map(float, input().split())
if o < b and o < l:
    print("Otavio")
elif b < o and b < l:
    print("Bruno")
elif l < o and l < b:
    print("Ian")
else:
    print("Empate")