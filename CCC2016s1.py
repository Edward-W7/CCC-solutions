st = input()
freq = [0] * 10000
anfreq = [0] * 10000
for i in st:
    freq[ord(i)] += 1
an = input()
ast = 0
inequal = 0
for i in an:
    if i == '*':
        ast += 1
    else:

        anfreq[ord(i)] += 1
for i in range(len(freq)):

    if freq[i] != anfreq[i]:
        if freq[i] > anfreq[i]:
            inequal += freq[i] - anfreq[i]
        else:
            ast = 999

if inequal == ast:
    print('A')
else:
    print('N')
