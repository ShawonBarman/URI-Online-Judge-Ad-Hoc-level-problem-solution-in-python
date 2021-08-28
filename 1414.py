#when a team wins a game, it gets 3 points
#if the game ends in a draw, both teams get 1 point
#the loser no points

# T mean the number of participating teams
# N mean the number of matches played
# next T lines contains the name of a team and the number of points the team got so far

while True:
    t, n = map(int, input().split())
    if t == 0:
        break
    totalpoint = 3 * n
    team_point = 0
    for i in range(t):
        name, point = input().split()
        team_point += int(point)
    print(totalpoint-team_point)