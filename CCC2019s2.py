def isprime(n):
    for i in range(2,int(n**(1/2))+1):
        if (n%i) == 0:
            return False
    return True
n = int(input())
for i in range(n):
    num = int(input())
    e = 0
    while(True):
        if isprime(num+e) and isprime(num-e):
            break
        e += 1
    print(str(num+e) + " " + str(num-e))
