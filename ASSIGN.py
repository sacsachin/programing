# !/usr/bin/python3

"""
https://www.spoj.com/problems/ASSIGN/
Assignment
"""

def solve(a, n):
    dp = [0 for _ in range((1<<n)+1)]
    dp[0] = 1

    for j in range(1, 1<<n):
        i = j
        idx = 0
        while i > 0:
            idx += 1&i
            i >>= 1
        for k in range(n):
            if a[idx-1][k] == 1 and j&(1<<k):
                dp[j] += dp[j&~(1<<k)]
    # print(dp)
    return dp[(1<<n)-1]

if __name__  == "__main__":
    t = int(input())
    while t:
        n = int(input())
        a = [[(lambda x: int(x))(x) for x in input().split()] for _ in range(n)]
        print(solve(a, n))
        t -= 1
