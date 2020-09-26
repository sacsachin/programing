# !/usr/bin/python3

"""
Zero one knapsack.
"""
def solve(n, w, profit, weight):
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    # print(dp)
    for i in range(1, n+1):
        for j in range(1, w+1):
            if weight[i] <= j:
                dp[i][j] = max(profit[i]+dp[i-1][j-weight[i]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    # print(profit)
    # print(weight)
    # for i in range(n+1):
        # print(dp[i])
    return dp[n][w]

if __name__ == "__main__":
    n = int(input())
    w = int(input())
    profit = [0]
    weight = [0]
    profit += [(lambda x: int(x))(x) for x in input().split(" ")]
    weight += [(lambda x: int(x))(x) for x in input().split(" ")]
    print(solve(n, w, profit, weight))
