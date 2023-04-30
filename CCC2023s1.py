n = int(input())
lane1 = [0]
lane2 = [0]
lane1 += [int(i) for i in input().split()]
lane2 += [int(i) for i in input().split()]
lane1.append(0)
lane2.append(0)

ans = 0

for i in range(1, n+1):
    if lane1[i] == 1:
        if i % 2 == 0:
            ans += 3 - lane1[i-1] - lane1[i+1]
        else:
            ans += 3 - lane1[i-1] - lane1[i+1] - lane2[i]
    if lane2[i] == 1:
        if i % 2 == 0:
            ans += 3 - lane2[i-1] - lane2[i+1]
        else:
            ans += 3 - lane2[i-1] - lane2[i+1] - lane1[i]

print(ans)
