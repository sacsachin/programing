#!/usr/bin/python3

"""
https://atcoder.jp/contests/abc176/tasks/abc176_c
Step
"""


def solve(a, n):
    ans = 0

    for i in range(1, n):
        if a[i] < a[i-1]:
            ans += a[i-1] - a[i]
            a[i] = a[i-1]

    return ans

if __name__ == "__main__":
    n = int(input())
    a = [(lambda x: int(x))(x) for x in input().split()]

    print(solve(a, n))
