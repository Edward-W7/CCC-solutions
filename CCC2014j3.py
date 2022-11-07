n = int(input())
ansa = 100
ansb = 100
for i in range(n):
    inpt = [int(i) for i in input().split()]
    a = inpt[0]
    b = inpt[1]
    if b>a:
        ansa -= b
    elif b<a:
        ansb -= a
print(ansa)
print(ansb)
