# !/usr/bin/python

"""
https://atcoder.jp/contests/abc179/tasks/abc179_b
B - Go to Jail
"""

def solve(n):
    count = 0
    p_d1, p_d2 = list(map(int, input().split()))
    if p_d1 == p_d2: count = 1
    n -= 1

    while n:
        d1, d2 = list(map(int, input().split()))
        if d1 == d2 and p_d1 == p_d2:
            count += 1
            if count == 3: return "Yes"
        elif d1 == d2: count = 1
        else: count = 0
        p_d1 = d1
        p_d2 = d2

        n -= 1

    return "No"

if __name__ == "__main__":
    n = int(input())

    print(solve(n))
