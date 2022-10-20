n = input()
inpt = [int(i) for i in input().split()]

freq = [0] * 20020
for i in inpt:
    freq[i] += 1

heightfreq = [0] * 40040
lenlist = set(inpt)
lenlist = sorted(list(lenlist))
if len(lenlist) == 1:
    print(*[int(len(inpt)/2), 1])

else:
    for i in range(len(lenlist)):
        for n in range(i, len(lenlist)):
            if n != i:
                heightfreq[lenlist[i] + lenlist[n]] += min(freq[lenlist[i]], freq[lenlist[n]])
            if n == i and freq[i] >= 2:
                heightfreq[lenlist[i] + lenlist[n]] += int(freq[lenlist[i]]/2)
    print(*[max(heightfreq), heightfreq.count(max(heightfreq))])

