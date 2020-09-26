# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/longest-common-prefix/
Longest Common Prefix
"""

def find_min_len(s):
    mi = s[0].__len__()
    for i in range(1, n):
        mi = min(mi, s[i].__len__())
    return mi

def solve(s):
    n = s.__len__()
    min_len = find_min_len(s, n)
    result = ""
    for i in range(min_len):
        for j in range(1, n):
            if s[j][i] != s[j-1][i]:
                return result
        result += s[0][i]
    return result

if __name__ == "__main__":
    s = [x for x in input().split(" ")]
    print(solve(s))
