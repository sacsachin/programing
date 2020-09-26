# !/usr/bin/python3

"""
Bredth first search.
https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/
Zero One BFS.
"""

from collections import deque

def zero_one_bfs(a, s):
    n = len(a)
    distance = [0 for _ in range(n)]
    dq  = deque()
    dq.append(s)
    distance[s]= 0
    print(a)

    while dq:
        u = dq.popleft()
        for v in range(len(a[u])):
            distance[a[u][v][0]] = min(distance[a[u][v][0]], distance[u]+a[u][v][1])
            if a[u][v][1] == 0:
                dq.appendleft(a[u][v][0])
            else:
                dq.append(a[u][v][0])

    return distance[::]

if __name__ == "__main__":
    n = int(input())
    a = [[(lambda x: tuple(map(int, x.split())))(x) for x in input().split(",")] for _ in range(n)]
    print(zero_one_bfs(a, 0))
