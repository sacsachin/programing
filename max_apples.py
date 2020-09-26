# !/usr/bin/python3

"""
A table composed of N x M cells, each having a certain quantity of apples, is given.
You start from the upper-left corner.
At each step you can go down or right one cell.
Find the maximum number of apples you can collect.
"""

def solve(a, n):
    m = len(a[0])
    dp = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] += dp[i][j-1]+a[i][j]
            elif j == 0:
                dp[i][j] =+ dp[i-1][j]+a[i][j]
            else:
                dp[i][j] += max(dp[i][j-1], dp[i-1][j])+a[i][j]
    # for i in range(n): print(dp[i])

    return dp[n-1][m-1]

if __name__ == "__main__":
    n = int(input())
    a = [[(lambda x: int(x))(x) for x in input().split()] for _ in range(n)]
    print(solve(a, n))
