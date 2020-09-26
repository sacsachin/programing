# !/usr/bin/python3

"""
https://www.spoj.com/problems/BINSTIRL/
BINSTIRL - Binary Stirling Numbers
http://www.cse.iitd.ernet.in/~mittal/stirling.html
"""

def solve(n, m):
    if m > n:
        return 0
    ans = (n-m)&((m-1)>>1)
    return 1 if ans == 0 else 0

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n, m = [(lambda x: int(x))(x) for x in input().split(" ")]
        print(solve(n, m))
        t -= 1
