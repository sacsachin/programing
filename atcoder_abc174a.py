# !/usr/bin/python3

"""
https://atcoder.jp/contests/abc174/tasks/abc174_a
Air Condetioner.
"""

def solve(n):
    if n >= 30: return "Yes"
    return "No"


if __name__ == "__main__":
    n = int(input())

    print(solve(n))
