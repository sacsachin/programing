#!/usr/bin/python3

"""
https://atcoder.jp/contests/abc176/tasks/abc176_a
Takoyaki
"""

import math

def solve(n, x, t):
    return int(math.ceil(n / x)) * t

if __name__ == "__main__":
    n, x, t = list(map(int, input().split()))
    print(solve(n, x, t))

