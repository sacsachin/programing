# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/largest-coprime-divisor/
Largest coprime divisor
"""
import math

def gcd(A, B):
    if B == 0:
        return A
    return gcd(B, A%B)

def solve(A, B):
    while gcd(A, B) is not 1:
        A = A // gcd(A,B)
    return A

if __name__ == "__main__":
    A = int(input())
    B = int(input())
    print(solve(A, B))

