# !/usr/bin/python3

"""
Given a sequence of N numbers – A[1] , A[2] , …, A[N] . Find the length of the longest non-decreasing sequence.
Dynamic Programing.
"""

def solve(a):
    n = len(a)
    dp = [0 for i in range(n)]
    dp[0] = 1
    for i in range(1, n):
        if a[i] > a[i-1]:
            dp[i] = dp[i-1]+1
        else:
            dp[i] = dp[i-1]
    # print(dp)
    return dp[n-1]

if __name__ == "__main__":
    a = [(lambda x: int(x))(x) for x in input().split()]
    print(solve(a))
