n = int(input())
low = []
high = []
inpt = [int(i) for i in input().split()]
inpt = sorted(inpt)
ans = []
if len(inpt)%2 == 0:
    low = inpt[:int(len(inpt)/2)]
    high = inpt[int(len(inpt) / 2):]
    for i in range(len(low)):
        ans.append(low[len(low)-i-1])
        ans.append(high[i])
    print(*ans)
else:
    low = inpt[:int(len(inpt)/2 + 1)]
    high = inpt[int(len(inpt) / 2) + 1:]
    for i in range(len(high)):
        ans.append(low[len(low)-i-1])
        ans.append(high[i])
    ans.append(low[0])
    print(*ans)
