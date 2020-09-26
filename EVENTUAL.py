# !/usr/bin/python3

"""
https://www.codechef.com/COOK120B/problems/EVENTUAL
Even-tual Reduction.
"""


def solve(s, n):
    s = list(s)
    ans = ord(s[0])

    for i in range(1, n):
        ans ^= ord(s[i])

    if ans != 0: print("NO")
    else: print("YES")

    return


if __name__ == "__main__":
    t = int(input())

    while t:
        n = int(input())
        s = input()
        solve(s, n)
        t -= 1
