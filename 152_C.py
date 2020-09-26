# !/usr/bin/python3

"""
https://atcoder.jp/contests/abc152/tasks/abc152_c
Low Elements.
"""
def solve(a, n):
    ans = 1
    mi = a[0]

    for i in range(1, n):
        mi = min(mi, a[i])
        if mi == a[i]: ans += 1

    return ans

if __name__ == "__main__":
    n = int(input())
    a = [(lambda x: int(x))(x) for x in input().split()]

    print(solve(a, n))
