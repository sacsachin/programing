"""
 * https://codeforces.com/contest/1382/problem/B
 * Sequential Nim.
"""

def solve(a, n):
    first = True

    for i in range(n-1):
        if a[i] == 1: first = not first
        else: break

    if first: print("First")
    else: print("Second")

if __name__ == "__main__":
    t = int(input())

    while(t):
        n = int(input())
        a = [(lambda x: int(x))(x) for x in input().split()]
        solve(a, n)
        t -= 1
