# !/usr/bin/python3

"""
Bredth first search.
https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/
Find level of each node.
"""

from collections import deque

def bfs(adj, s):
    n = len(adj)
    level = [float("inf") for _ in range(n)]
    visited = [False for _ in range(n)]
    # start
    q = deque()
    q.appendleft(s)
    # print(s)
    level[s] = 0
    visited[s] = True
    while q:
        node = q.pop()
        for i in range(len(adj[node])):
            if visited[adj[node][i]] == False:
                level[adj[node][i]] = level[node]+1
                q.append(adj[node][i])
                # print(a[node][i])
                visited[adj[node][i]] = True
    return level[::]

if __name__ == "__main__":
    n = int(input())
    a = [[(lambda x: int(x))(x) for x in input().split()] for _ in range(n)]
    print(bfs(a, 0))
