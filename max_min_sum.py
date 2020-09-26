# !/usr/local/bin/python3

"""
https://atcoder.jp/contests/abc151/tasks/abc151_e
Max Min Sum.
"""

MOD = int(1e9+7)

def nCk(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n]*(finv[n-k]*finv[k]%MOD)%MOD

def solve():
    a.sort()

    for i in range(2, MAX_N):
        fac[i] = fac[i-1]*i%MOD
        inv[i] = MOD-(inv[MOD%i])*(MOD//i)%MOD
        finv[i] = finv[i-1]*inv[i]%MOD

    max_x = 0
    for i in range(k-1, n):
        max_x = (max_x+a[i]*nCk(i, k-1))%MOD

    min_x = 0
    for i in range(n-k+1):
        min_x = (min_x+a[i]*nCk(n-i-1, k-1))%MOD

    return((max_x-min_x)%MOD)

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    a = [(lambda x: int(x))(x) for x in input().split()]
    MAX_N = n+5
    fac = [1, 1]+[0 for _ in range(MAX_N)]
    finv = [1, 1]+[0 for _ in range(MAX_N)]
    inv = [0, 1]+[0 for _ in range(MAX_N)]
    print(solve())
