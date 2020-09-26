# !/usr/bin/python3

"""
You are on a staircase. Each time u can jump to 1 or 2 staircase. Find the numbers of ways to reach top.
"""
def solve(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(solve(n))

