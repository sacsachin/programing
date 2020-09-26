# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/palindrome-string/
Palindrome String.
"""

import re


def solve(s):
    pattern = re.compile("[\W_]+")
    s = pattern.sub("", s)
    n = s.__len__()
    print(s)
    for i in range(n//2):
        if s[i].lower() != s[n-i-1].lower():
            return 0
    return 1

if __name__ == "__main__":
    s = input()
    print(solve(s))
