weight = int(input())
n = int(input())
ans = -1
w = 0
car = []
for i in range(n):
    car.append(int(input()))
for i in range(len(car)):
    if i<=3:
        w += car[i]
        if w >weight:
            ans = i
            break
    else:
        w += car[i]
        w -= car[i-4]
        if w >weight:
            ans = i
            break
if ans == -1:
    print(n)
else:
    print(ans)
