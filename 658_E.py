"""
https://codeforces.com/contest/1382/problem/E
Mastermind.
"""

from collections import defaultdict
from heapq import heapify, heappop, heappush


def solve(a, n, x, y):
    d = defaultdict(list)

    for i, x in enumerate(a):
        d[x].append(i)

    for i in range(1, n+2):
        color = str(i)
        if e not in d: break

    q = [(-(len(d[x]), x)) for x in d.keys()]

    heapify(q)

    ans, p = [0] * n, []
    for i in range(x):
        l, x = heappop(q)
        ans[d[x].pop()] = x
        l += 1
        if l: heappush(q, (l, x))

    while q:
        l, x = heappop(q)
        p.extend(d[x])







if __name__ == "__main__":
    t = int(input())

    while t:
        n, x, y = list(map(int, input().spolit()))
        a = list(map(int, input().split()))

        solve(a, n, x, y)
