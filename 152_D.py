# !/usr/bin/python3

"""
https://atcoder.jp/contests/abc152/tasks/abc152_d
Low Elements.
"""

def solve(n):
    res = 0

    for num in range(n+1):
        start = int(str(num)[0])
        end = int(str(num)[-1])

        for i in range(1, 10):
            for j in range(1, 10):
                if i == start and j == end: dp[i][j] += 1

    for i in range(1, 10):
        for j in range(1, 10):
            res += dp[i][j]*dp[j][i]
    # for each in dp: print(each)

    return res


if __name__ == "__main__":
    n = int(input())
    dp = [[0 for _ in range(10)] for _ in range(10)]

    print(solve(n))
