# !/usr/bin/python3

def binary_exp(a, b):
    res = 1
    while b > 0:
        if b&1:
            res *= a
        a *= a
        b >>= 1
    return res

if  __name__ == "__main__":
    A = int(input())
    B = int(input())

    print(binary_exp(A, B))
