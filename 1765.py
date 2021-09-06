while True:
    t = int(input())
    if t == 0:
        break
    for i in range(t):
        q, a, b = map(float, input().split())
        ans = (((a+b)*5)/2)*q
        print(f"Size #{i+1}:")
        print("Ice Cream Used: {:.2f} cm2".format(ans))
    print()