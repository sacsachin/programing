"""
https://codeforces.com/contest/1382/problem/C2
Prefix Flip 2
"""

def solve(a, b, n):
    op1 = []
    op2 = []

    a += '0'
    b += '0'

    for i in range(1, n+1):
        if a[i] != a[i-1]: op1.append(i)
        if b[i] != b[i-1]: op2.append(i)

    op1 += op2[::-1]

    print(len(op1), ' '.join([str(x) for x in op1]))

    return


if __name__ == "__main__":
    t = int(input())

    while t:
        n = int(input())
        a = input()
        b = input()
        solve(a, b, n)
        t -= 1
