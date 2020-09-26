# !/usr/bin/pyhton3

"""
LCS Problem
Dynamic Programing.
"""

def lcs(s1, n, s2, m):
    dp  = [[0 for j in range(m+1)] for i in range(n+1)]
    # for i in range(n+1): print(dp[i])
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 0 or j == 0:
                continue
            elif s1[i] == s2[j]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    # for i in range(n+1): print(dp[i])
    return dp[n][m]

if __name__ == "__main__":
    from time import perf_counter
    # s1 = input()
    # s2 = input()
    start = perf_counter()
    s1 = "abgfcxyzxyz"
    s2 = "abksgmnflpcxyzxyz"
    n = len(s1)
    m = len(s2)
    s1 = " "+s1
    s2 = " "+s2
    print(lcs(s1, n, s2, m))
    print(perf_counter()-start)
