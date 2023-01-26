from math import factorial

fav = int(input())
g = int(input())
score = [0] * 5
rounds = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
ways = 0
for i in range(g):
    team1, team2, score1, score2 = map(int, input().split())
    rounds.remove([team1, team2])
    if score1 > score2:
        score[team1] += 3
    elif score2 > score1:
        score[team2] += 3
    else:
        score[team1] += 1
        score[team2] += 1


def game(score, r):
    ans = []
    for i in r:
        for k in range(1, 4):
            cur = (score[:])
            if k == 1:
                cur[i[0]] += 1
                cur[i[1]] += 1
            elif k == 2:
                cur[i[0]] += 3
            elif k == 3:
                cur[i[1]] += 3
            ans.append(cur)
    return ans


for i in range(len(game(score, rounds))):
    curr = (rounds[:])
    curr.pop(i // 3)
    score3 = (game(score, rounds)[i])[:]

    for j in range(len(game(score3, curr))):
        curr2 = (curr[:])
        curr2.pop(j // 3)
        score4 = (game(score3, curr)[j])[:]

        for k in range(len(game(score4, curr2))):
            curr3 = (curr2[:])
            curr3.pop(k // 3)
            score5 = (game(score4, curr2)[k])[:]

            for l in range(len(game(score5, curr3))):
                curr4 = (curr3[:])
                curr4.pop(l // 3)
                score6 = (game(score5, curr3)[l])[:]

                for m in range(len(game(score6, curr4))):
                    curr5 = (curr4[:])
                    curr5.pop(m // 3)
                    score7 = (game(score6, curr4)[m])[:]

                    for n in range(len(game(score7, curr5))):
                        curr6 = (curr5[:])
                        curr6.pop(n // 3)
                        score8 = (game(score7, curr5)[n])[:]

                    if curr5 == [] and score7.index(max(score7)) == fav and score7.count(score7[fav]) == 1:
                        ways += 1
                if curr4 == [] and score6.index(max(score6)) == fav and score6.count(score6[fav]) == 1:
                    ways += 1
            if curr3 == [] and score5.index(max(score5)) == fav and score5.count(score5[fav]) == 1:
                ways += 1
        if curr2 == [] and score4.index(max(score4)) == fav and score4.count(score4[fav]) == 1:
            ways += 1
    if curr == [] and score3.index(max(score3)) == fav and score3.count(score3[fav]) == 1:
        ways += 1
if g == 0:
    print(int(factorial(6) / 5))
else:
    print(int(ways / factorial(6 - g)))
