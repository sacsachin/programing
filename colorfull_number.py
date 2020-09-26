# !/usr/bin/python3

"""
Colorful Number
https://www.interviewbit.com/problems/colorful-nber/
"""

def solve(n):
    s = set()
    power = 10
    remainder = 1

    while True:
        num = n
        while num >= remainder:
            t = num%power
            prod = 1
            while t > 0:
                prod *= t%10
                t //= 10
            if s.__contains__(prod): return 0
            s.add(prod)
            num //= 10
        if power > n: break
        power *= 10
        remainder *= 10

    return 1

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
