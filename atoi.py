# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/atoi/
Atoi
"""

def solve(s):
    MAX_INT = 2147483647
    MIN_INT = -2147483648

    s = s.strip()
    s = s.split()[0]
    ans = 0
    neg = False
    n = len(s)
    if s[0] == '-':
        neg = True
        s = s[1:n]
        n = len(s)
    if not s:
        return 0
    if s[0] == '+':
        s = s[1:n]
        n = len(s)
    if not s:
        return 0
    for i in range(n):
        if ord(s[i]) >= 48 and ord(s[i]) <=57:
            temp = ord(s[i])-48
            ans = ans*10+temp
        else:
            break
    if not neg and ans > MAX_INT:
        return MAX_INT
    if neg and ans > MAX_INT+1:
        return MIN_INT
    return ans if not neg else -ans

if __name__ == "__main__":
    s = input()
    print(solve(s))
