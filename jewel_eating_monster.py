# !/usr/bin/python3

"""
https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1723
https://cp-algorithms.com/algebra/binary-exp.html
"""

def solve(x, y, n, c):
    t= (x%c)*(y%c)
    ans = 1
    while n > 0:
        if n&1:
            ans = (ans*t)%c
        t = (t*t)%c
        n >>= 1

    return ans


if __name__ == "__main__":
    A = [(lambda x: int(x))(x) for x in input().split(" ")]
    print(solve(A[0], A[1], A[2], A[3]))
