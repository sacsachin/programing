# !/usr/bin/python3

"""
https://www.spoj.com/problems/MICEMAZE/
MICEMAZE - Mice and Maze
"""

def solve(n, ep, t, c, maze):
    for each in maze:
        print(each)

if __name__ == "__main__":
    n = int(input())
    ep = int(input())
    t = int(input())
    c = int(input())
    temp = c
    maze = [[0 for _ in range(n+1)] for _ in range(n+1)]
    while temp > 0:
        i, j, k = list(map(int, input().split()))
        maze[i][j] = k
        temp -= 1
    print(solve(n, ep, t, c, maze))
