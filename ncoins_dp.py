# !/usr/bin/python3

"""
Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), or report that it’s not possible to select coins in such a way that they sum up to S.
Dynamic Programing
"""

def solve(coins, s):
    n = len(coins)
    dp = [float("inf") for _ in range(s+1)]
    dp[0] = 0

    for i in range(1, s+1):
        for j in range(0, n):
            if coins[j] <= s:
                dp[i] = min(dp[i], dp[i-coins[j]]+1)
    return dp[s]

if __name__ == "__main__":
    coins = [(lambda x: int(x))(x) for x in input().split()]
    s = int(input())
    print(solve(coins, s))
