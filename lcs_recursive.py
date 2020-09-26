# !/usr/bin/python3

"""
LCS Problem.
"""

def lcs(s1, i, n, s2, j, m):
    if i == n or j == m:
        return 0
    elif s1[i] == s2[j]:
        return 1+lcs(s1, i+1, n, s2, j+1, m)
    else:
        return max(lcs(s1, i, n, s2, j+1, m), lcs(s1, i+1, n, s2, j, m))

if __name__ == "__main__":
    # s1 = input()
    # s2 = input()
    from time import perf_counter
    start = perf_counter()
    s1 = "abgfcxyzxyz"
    s2 = "abksgmnflpcxyzxyz"
    n = len(s1)
    m = len(s2)
    print(lcs(s1, 0, n, s2, 0, m))
    print(perf_counter()-start)
