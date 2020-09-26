# !/usr/bin/python3

"""
https://cp-algorithms.com/algebra/binary-exp.html
http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3671
"""

def binary_exp(a, b, m):
    res = 1%m
    a = a%m
    while b > 0:
        if b&1:
            res = (res*a)%m
        a = (a*a)%m
        b >>= 1
    return res%m

if  __name__ == "__main__":
    A = int(input())
    B = int(input())
    M = int(input())

    print(binary_exp(A, B, M))
