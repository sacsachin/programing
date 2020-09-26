# !/usr/bin/python3

"""
https://www.spoj.com/problems/AE2A/
AE2A - Dice
Dynamic Programing.
"""

from sys import stdin, stdout

input = stdin.readline()

def solve(n, k):
    pass

if __name__ == "__main__":
    t = int(input())
    while t:
        n, k = tuple(map(int, input().strip().split()))
        print(solve(n, k))
        t -= 1
