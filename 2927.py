numStudents, numPC, x, y = map(int, input().split())
if (numPC-x)-y > numStudents:
    print("Igor feliz!")
else:
    if x > y/2:
        print("Caio, a culpa eh sua!")
    else:
        print("Igor bolado!")