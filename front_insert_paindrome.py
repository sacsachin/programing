# !/usr/bin/pyhthon3

def lps(s):
    n = s.__len__()
    lps = [0]*n
    length = 0
    i = 1
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    return lps[-1]

def solve(s):
    n = s.__len__()
    s_ = s[::-1]
    c = s+"$"+s_
    longest_match = lps(c)
    return n-longest_match

if __name__ == "__main__":
    s = input()
    print(solve(s))
