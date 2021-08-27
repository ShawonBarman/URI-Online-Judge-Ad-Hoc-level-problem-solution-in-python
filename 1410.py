# An attacking player is offside if he is nearer to his opponents’ goal line than the second last opponent.
# A player is not offside if
#     (1)he is level with the second last opponent or
#     (2)he is level with the last two opponents.

# A mean the number of attacking
# D mean defending players involved in the play
# A integers Bi separated by single spaces, indicating the distances of the attacking players to the goal line
# D integers Cj separated by single spaces, indicating the distances of the defending players to the goal line

while True:
    a, d = map(int, input().split())
    if a == 0 and d == 0:
        break
    b = list(map(int, input().split()))[:a]
    b.sort()
    c = list(map(int, input().split()))[:d]
    c.sort()
    if b[0] >= c[0] and b[0] >= c[1]:
        print("N")
    elif b[0] >= c[1]:
        print("N")
    else:
        print("Y")