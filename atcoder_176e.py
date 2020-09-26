# !/usr/bin/python3

"""
https://atcoder.jp/contests/abc176/tasks/abc176_e
Bomber
"""


def solve(h, w, m, bomb):
    row = dict()
    for each in bomb:
        row.setdefault(eacch[0], 0)
        row[each[i]] += 1

    col = dict()
    for each in bomb:
        col.setdefault(each[1], 0)
        col[each[1]] += 1

    row_max = max(row, key=row.get)
    col_max = max(col, key=col.get)

    if(row[row_max] > col[col_max]):
        for i in range(1, w + 1):



if __name__ == "__main__":
    h, w, m = map(int, input().split())
    bomb = [[(lambda x: int(x))(x)  for x in input().split()] for _ in m]


