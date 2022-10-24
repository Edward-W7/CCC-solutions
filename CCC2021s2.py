leng = int(input())
wid = int(input())
n = int(input())
rowbad = []
colbad = []
stroke = []
row = []
col = []
ans = 0
for i in range(n):
    inpt = input().split()
    stroke.append(inpt)
for i in stroke:
    if i[0] == 'R':
        rowbad.append(int(i[1]))
    elif i[0] == 'C':
        colbad.append(int(i[1]))
colbad.sort()
rowbad.sort()
colfreq = [0] * 5000000
rowfreq = [0] * 5000000
for i in colbad:
    colfreq[i] += 1
for i in rowbad:
    rowfreq[i] += 1
for i in range(len(colfreq)):
    colfreq[i] = colfreq[i] % 2
for i in range(len(rowfreq)):
    rowfreq[i] = rowfreq[i] % 2
vert = colfreq.count(1)
n = 0
for i in range(1, leng+1):
    if rowfreq[i] == 1:
        ans += wid-vert
    else:
        ans += vert
print(ans)
