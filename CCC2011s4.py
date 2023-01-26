#this solution is correct on the official cemc ccc test data, but it does not pass additional tests on dmoj
import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log, inf

sys.setrecursionlimit(690000000)


# actual code

blood = [int(i) for i in stdin.readline().split()]
patient = [int(i) for i in stdin.readline().split()]
ans = 0


def allo(a, b):
    global ans
    global blood
    global patient
    alo = min(blood[a], patient[b])
    blood[a] -= alo
    patient[b] -= alo

    ans += alo


allo(0, 0)

allo(1, 1)

allo(2, 2)

allo(4, 4)

allo(1, 3)
allo(2, 3)
allo(3, 3)

allo(1, 5)
allo(4, 5)
allo(5, 5)

allo(2, 6)
allo(4, 6)
allo(6, 6)

allo(0, 1)
allo(0, 2)
allo(0, 3)
allo(0, 4)
allo(0, 5)
allo(0, 6)

ans += min(sum(blood), patient[7])

print(ans)
