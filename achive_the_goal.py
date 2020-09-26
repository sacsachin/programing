# !/usr/bin/python3

"""
https://atcoder.jp/contests/abc151/tasks/abc151_b
Achive the goal.
"""

def splve(n, k, m, a):
    sm = sum(a)
    remaining = m*n-sm

    if remaining < 0: return 0
    elif remaining <= k: return remaining
    else:  return -1

if __name__ == "__main__":
    n, k, m = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    print(solve(n, k, m, a))
