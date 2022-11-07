n = int(input())
group1 = input().split()
group2 = input().split()
dict = {}
good = True
for i in range(n):
    if (group1[i] not in dict or dict[group1[i]] == group2[i]) and group1[i] != group2[i]:
        dict[group1[i]] = group2[i]
        dict[group2[i]] = group1[i]
    else:
        good = False
if good:
    print('good')
else:
    print('bad')
