# !/usr/bin/python3

"""
https://www.spoj.com/problems/BUGLIFE/
BUGLIFE - A Bug’s Life
"""

def solve(n, m a):
    pass


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, m = [(lambda x: int(x))(x) for x in input.split(" ")]
        temp = m
        pair = []
        while temp > 0:
            pair.append([(lambda x: int(x))(x) for x in input().split(" ")])
            temp -= 1
        solve(n, m, pair)
        t -= 1
