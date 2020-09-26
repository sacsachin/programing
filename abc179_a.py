# !/usr/bin/python3

"""
https://atcoder.jp/contests/abc179/tasks/abc179_a
A - Plural Form .
"""

def solve(s):
    if s[-1] == 's': print(s + "es")
    else: print(s + 's')

    return


if __name__ == "__main__":
    s = input()
    solve(s)
