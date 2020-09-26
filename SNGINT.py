# !/usr/bin/python3

"""
https://www.spoj.com/problems/SNGINT/
SNGINT - Encode Integer
"""
import math

def solve(n):
    if n < 10:
        if n == 0:
            return print("10")
        else:
            return print(n)
    a = [None]*20
    k = 0
    for i in range(9, 1, -1):
        while n%i == 0:
            n //= i
            a[k] = i
            k += 1
    if n > 10:
        return print("-1")
    for i in range(k-1, -1, -1):
        print(a[i], end="")
    return print(end="\n")

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        solve(n)
        t -= 1
