# !/usr/bin/python3

"""
https://leetcode.com/problems/zigzag-conversion/
"""

def solve(s, row):
    if row == 1:
        return s
    n = len(s)
    rows = ["" for _ in range(min(row, n))]
    is_down = False
    curr_row = 0
    for i in range(n):
        rows[curr_row] += s[i]
        if curr_row in (0, row-1):
            is_down = not is_down
        curr_row += 1 if is_down else -1

    ans = ""
    for each in rows:
        ans += each
    return ans

if __name__ == "__main__":
    s = input()
    row = int(input())
    print(solve(s, row))
