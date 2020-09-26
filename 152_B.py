# !/usr/bin/python3

"""
https://atcoder.jp/contests/abc152/tasks/abc152_b
Comparing starings.
"""

def solve(n, m):
    if n > m: print(f"{m}"*n)
    elif m >= n: print(f"{n}"*m)

    return

if __name__ == "__main__":
    n, m = list(map(int, input().split()))

    solve(n, m)
