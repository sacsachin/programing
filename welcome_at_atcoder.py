# !/usr/bin/python3

"""
https://atcoder.jp/contests/abc151/tasks/abc151_c
Welcome at atcoder
"""


if __name__ == "__main__":
    n, m = list(map(int, input().split()))

    accepted = [False for _ in range(n+5)]
    wrong = [0 for _ in range(n+5)]
    ac = wa = 0

    for _ in range(m):
        p, s = input().split()
        p = int(p)

        if accepted[p]: continue
        elif s == "WA": wrong[p] += 1
        elif s == "AC":
            ac += 1
            wa += wrong[p]
            accepted[p] = True

    print(f"{ac} {wa}")

