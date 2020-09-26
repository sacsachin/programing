# !/usr/bin/python3

"""
https://www.spoj.com/problems/ABCDEF/
ABCDEF
"""

from bisect import bisect_right as br
from bisect import bisect_left as bl


def solve(a, n):
    ans = 0
    ab = [0]*n**2
    ef = [0]*n**2
    count = 0
    for i in range(n):
        for j in range(n):
            ab[count] = a[i]*a[j]
            ef[count] = a[i]+a[j]
            count += 1
    # print(ab)
    # print(ef)
    a_b = len(ab)
    e_f = len(ef)
    ab = ab*n
    ef = ef*n
    # print(ab)
    # print(ef)

    count = 0
    for i in range(n):
        for j in range(a_b):
            ab[count] += a[i]
            ef[count] *= a[i]
            count += 1
    a_b= len(ab)
    e_f = len(ef)
    # print(ab)
    # print(ef)
    ab.sort()
    ef.sort()
    for i in range(a_b):
        ans += br(ef, ab[i])-bl(ef, ab[i])

    return ans

if __name__ == "__main__":
    n = int(input())
    numbers = [None]*n
    temp = 0
    while temp < n:
        numbers[temp] = int(input())
        temp += 1
    print(solve(numbers, n))
