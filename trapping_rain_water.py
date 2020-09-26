# !/usr/bin/python3

"""
https://leetcode.com/problems/trapping-rain-water/
Trapping rain water.
"""

def solve(a):
    n = len(a)
    left_max = [0 for _ in range(n)]
    right_max = [0 for _ in range(n)]
    ans = lm = rm = 0

    for i in range(n):
        left_max[i] = max(a[i], lm)
        lm = left_max[i]

    for i in range(n-1, -1, -1):
        right_max[i] = max(rm, a[i])
        rm = right_max[i]

    for i in range(n):
        ans += abs(a[i]-min(left_max[i], right_max[i]))

    return ans

if __name__ == "__main__":
    a = list(map(int, input().split()))
    print(solve(a))
