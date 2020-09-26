# !/usr/bin/python3

"""
https://atcoder.jp/contests/abc152/tasks/abc152_e
Flatten.
"""

MOD = int(1e9+7)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def inverse(a, b, x=None, y=None):
    if b == 0:
        x = 1
        y = 0
        return (a, x, y);
    d, x1, y1 = inverse(b, a % b, x, y)
    x = y1
    y = x1-y1*(a//b)
    return (d, x, y)

def solve(a, n):
    lcm = 1

    for i in range(n):
        g = gcd(lcm, a[i])
        inv = inverse(g, MOD)[1]
        inv = (inv%MOD+MOD)%MOD
        lcm = lcm*a[i]*int

    ans = 0
    for i in range(n):
        inv = inverse(a[i], MOD)[1]
        inv = (inv%MOD+MOD)%MOD
        ans = ans+(lcm*inv)%MOD

    return ans%MOD

if __name__ == "__main__":
    n = int(input())
    a = [(lambda x: int(x))(x) for x in input().split()]
    print(solve(a, n))
