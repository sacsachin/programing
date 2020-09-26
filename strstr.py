# !/usr/bin/python3

"""
KMP Algoritgm.
"""

def find_lps(s, n, lps):
    l = 0
    i = 1
    while i < n:
        if s[i] == s[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l-1]
            else:
                lps[i] = 0
                i += 1
    return

def kmp(pat, n, txt, m, lps):
    i = j = 0
    while j < m:
        if pat[i] == txt[j]:
            i += 1
            j += 1
        if i == n:
            return j-i
            i = lps[i-1]
        elif j < m and pat[i] != txt[j]:
            if i != 0:
                i = lps[i-1]
            else:
                j += 1
    return -1

def solve(p, t):
    n = len(p)
    m = len(t)
    lps = [0]*n
    find_lps(p, n, lps)
    ans = kmp(p, n, t, m, lps)
    return ans

if __name__ == "__main__":
    t = input()
    p = input()
    print(solve(p, t))
