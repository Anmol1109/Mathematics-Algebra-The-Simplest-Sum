from math import floor
from math import log

def bj(k, n):
    return floor(log(n * k - n + 1, k))

def st(k, j):
    return (k**j - 1) // (k - 1)

def bf(k, j):
    return (k**(j + 1) - k * j - k + j) // (k - 1)**2

def bs(k, l, r):
    x = bj(k, l)
    y = bj(k, r)
    
    if x == y:
        return bf(k, x) * (r - l + 1)
    
    sx, sy, s = bf(k, x) * (st(k, x + 1) - l), bf(k, y) * (r - st(k, y) + 1), 0
    
    if y - x > 1:
        s1 = k**(2 * y + 1) + y * k**y + (x + 1) * k**(x + 3)
        s2 = k**(2 * x + 3) + y * k**(y + 2) + (x + 1) * k**(x + 1)
        
        s = (s1 - s2) // ((k - 1)**2 * (k**2 - 1))
    
    return sx + s + sy

for _ in range(int(input())):
    k, l, r = map(int, input().split())
    print(bs(k, l, r) % (10**9 + 7))
