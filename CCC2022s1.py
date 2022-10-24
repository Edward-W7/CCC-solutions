N = int(input())
ways = 0
if (N % 4 == 0):
	ways += 1
for i in range(0,N,4):
	if ((N - i) % 5 == 0):
		ways += 1
print(ways)
