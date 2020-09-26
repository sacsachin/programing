#!/usr/bin/python3

"""
https://atcoder.jp/contests/abc176/tasks/abc176_b
Multiuple of 9.
"""

def solve(num):
    res = 0
    for x in num:
        dig = int(x)
        res = (res + dig) % 9

    if res == 0: return "Yes"
    return "No"


if __name__ == "__main__":
    num = input()
    print(solve(num))
