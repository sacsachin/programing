# /usr/bin/python3

"""
https://leetcode.com/problems/longest-palindromic-substring/
Longest Palindromic Substring.
"""

def solve(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    max_len = 1
    start = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_len = 2

    k = 3
    while k <= n:
        i = 0
        while i < n-k+1:
            j = i+k-1
            if dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
                if k > max_len:
                    start = i
                    max_len = k
            i += 1
        k += 1
    return s[start: start+max_len]

if __name__ == "__main__":
    s = input()
    print(solve(s))
