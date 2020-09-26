# !/usr/bin/pyhton3

"""
https://atcoder.jp/contests/abc174/tasks/abc174_b
Distance.
"""

import math

def solve(x, y):
    return math.sqrt(x*x + y*y)

if __name__ == "__main__":
    ans = 0

    n, d = list(map(int, input().split()))

    while n:
        x, y = list(map(int, input().split()))
        ans += 1 if solve(x, y) <= d else 0
        n -= 1

    print(ans)
