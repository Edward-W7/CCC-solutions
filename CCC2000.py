x = int(input())
n = int(input())
coins = []
for i in range(n):
    coins.append(int(input()))
dp = [float('inf') for i in range(x+1)]
dp[0] = 0
for i in coins:
    dp[i] = 1

for i, vi in enumerate(dp):
    mini = float('inf')
    for c in coins:
        if i-c < 0:
            pass
        else:
            if dp[i-c] != float('inf'):
                mini = min(mini, dp[i-c] + 1)
    dp[i] = min(dp[i], mini)
if dp[-1] == float('inf'):
    print("Roberta acknowledges defeat.")
else:
    print(f"Roberta wins in {dp[-1]} strokes.")
