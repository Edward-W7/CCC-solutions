qtype = int(input())
ans = 0
n = int(input())
dmoj = sorted([int(i) for i in input().split()])
peg = sorted([int(i) for i in input().split()])
if qtype == 1:
    for i in range(len(dmoj)):
        ans += max([dmoj[i], peg[i]])
    print(ans)
else:
    for i in range(len(dmoj)):
        ans += max(dmoj[i], peg[n-i-1])
    print(ans)
