# !/usr/bin/python3

"""
https://atcoder.jp/contests/abc174/tasks/abc174_c
Repsept.
"""

def solve(k):
    num = k

    if num % 10 not in (1, 3, 7): return -1

    multiple = 7
    count = 0

    while True:
        count += 1
        if multiple % k == 0 or k % multiple == 0: break
        multiple = 10 * multiple + 7

    return count


if __name__ == "__main__":
    k = int(input())

    print(solve(k))
