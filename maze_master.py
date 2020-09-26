# !/usr/bin/python3

"""
https://atcoder.jp/contests/abc151/tasks/abc151_d
Maze Master.
"""

from collections import deque
from copy import deepcopy

def bfs(chw, i, j):
    dq = deque()

    dq.append([i, j])
    chw[i][j] = '#'

    dist = [[-1 for _ in range(w)] for _ in range(h)]
    dist[i][j] = 0

    # for each in dist: print(each)

    while dq:
        y, x = dq.popleft()
        for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ny = y+dy
            nx = x+dx
            if 0 <= nx < w and 0 <= ny < h and chw[ny][nx] == '.':
                dq.append([ny, nx])
                chw[ny][nx] = '#'
                dist[ny][nx] = dist[y][x]+1

    # for each in dist: print(each)
    temp_ans = 0
    for each in dist:
        temp_ans = max(temp_ans, max(each))

    return temp_ans

def solve(h, w, hw):
    ans = 0
    for i in range(h):
        for j in range(w):
            if hw[i][j] == '.':
                chw = deepcopy(hw)
                dist = bfs(chw, i, j)
                ans = max(dist, ans)
    return ans

if __name__ == "__main__":
    h, w = list(map(int, input().split(" ")))
    hw = [list(input()) for _ in range(h)]
    print(solve(h, w, hw))
