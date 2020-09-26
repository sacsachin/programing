# !/usr/bin/python3

"""
https://atcoder.jp/contests/abc174/tasks/abc174_d
Alter Alter.
"""

def solve(a, n):
    count = 0

    end = n-1
    for i in range(n):
        if end <= i: break
        if a[i] == 'W':
            for j in range(end, i-1, -1):
                if i == j: return count
                if a[j] == 'R':
                    count += 1
                    end -= 1
                    break
    return count

if __name__ == "__main__":
    n = int(input())
    a = list(input())

    print(solve(a, n))
