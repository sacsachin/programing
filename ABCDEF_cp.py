# !/usr/bin/python3

"""
https://www.spoj.com/problems/ABCDEF/
ABCDEF
"""
from sys import stdin, stdout
from bisect import bisect_right as br
from bisect import bisect_left as bl


def solve(a, n):
    ans = 0
    ab = []
    ef = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ab.append(a[i]*a[j]+a[k])
                if a[k] != 0:
                    ef.append((a[i]+a[j])*a[k])
    # print(ab)
    # print(ef)
    ab.sort()
    ef.sort()
    i = 0
    while i < n**3:
        lo = bl(ab, ab[i])
        hi = br(ab, ab[i])
        ans += (hi-lo)*(br(ef, ab[i])-bl(ef, ab[i]))
        i = hi

    return ans

if __name__ == "__main__":
    # from time import perf_counter
    # start = perf_counter()
    n = int(stdin.readline())
    # n = int(input())
    numbers = [None]*n
    temp = 0
    while temp < n:
        numbers[temp] = int(stdin.readline())
        # numbers[temp] = int(input())
        temp += 1
    # print(solve(numbers, n))
    stdout.write(str(solve(numbers, n))+"\n")
    # end = perf_counter()
    # print(end-start)
