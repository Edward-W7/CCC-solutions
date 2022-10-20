n = int(input())
team1 = [int(i) for i in input().split()]
team2 = [int(i) for i in input().split()]
ans = 0
team1total = 0
team2total = 0
for i in range(n):
    team1total += team1[i]
    team2total += team2[i]
    if team2total == team1total:
        ans = i + 1
print(ans)
