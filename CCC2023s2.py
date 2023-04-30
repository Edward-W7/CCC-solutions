from sys import stdin
n = int(stdin.readline())
mount = [int(i) for i in stdin.readline().split()]

symm = []
for i in range(n*2-1):
    symm.append([])

i = 0
while i < 2*n:
    j = 0
    if i < n:
        newi = i
    else:
        j = i + 1 - n

        newi = n-1
    while j <= n and newi >= 0:
        try:
            symm[i].append(abs(mount[newi] - mount[j]))
            newi -= 1
            j += 1
        except:
            break
        if j > newi + 1 or j > i // 2:
            break

    i += 1


for i in range(len(symm)):
    symm[i].reverse()
    for j in range(len(symm[i])-1):
        symm[i][j+1] = symm[i][j] + symm[i][j+1]

ans = []
for i in range(n):
    mn = float('inf')
    for j in range(2*n-1):
        if len(symm[j])*2-1 >= i and j % 2 == i % 2:
            mn = min(mn, symm[j][min(i//2, len(symm[j]) - 1)])
    ans.append(mn)

print(*ans)
