# !/usr/bin/python3

import re


def solve(s):
    n = re.compile(r"^[+-]?[0-9]*[\.]?[0-9]+(([Ee][+-]?)?[0-9]+)?[0-9]*$")
    n = n.strip()
    if n.match(s):
        return True
    return False

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        print(solve(s))
