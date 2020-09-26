# !/usr/bin/python3

"""
LCS Problem.
Memoization.
"""

def lcs(s1, i, n, s2, j, m, dp):
    if i == n or j == m:
        return 0
    elif s1[i] == s2[j]:
        if dp[i+1][j+1] != -1:
            dp[i][j] = 1+dp[i+1][j+1]
        else:
            dp[i][j] = 1+lcs(s1, i+1, n, s2, j+1, m, dp)
    else:
        left = right = 0
        if dp[i][j+1] != -1:
            right = dp[i][j+1]
        else:
            right = lcs(s1, i, n, s2, j+1, m, dp)
        if dp[i+1][j] != -1:
            left = dp[i+1][j]
        else:
            left = lcs(s1, i+1, n, s2, j, m, dp)
        dp[i][j] = max(left, right)
    return dp[i][j]

if __name__ == "__main__":
    from time import perf_counter
    # s1 = input()
    # s2 = input()
    start = perf_counter()
    s1 = "abgfcxyzxyz"
    s2 = "abksgmnflpcxyzxyz"
    n = len(s1)
    m = len(s2)
    dp = [[0 if i == n or j == m else -1 for j in range(m+1)] for i in range(n+1)]
    print(lcs(s1, 0, n, s2, 0, m, dp))
    print(perf_counter()-start)
    # for i in range(n+1): print(dp[i])
