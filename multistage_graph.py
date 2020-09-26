# !/usr/bin/python3

"""
Multistage Graph.
https://www.youtube.com/watch?v=9iE9Mj4m8jk&list=PLJULIlvhz0rE83NKhnq7acXYIeA0o1dXb&index=2
"""

def multistage_graph():
    stages = 4
    nodes = 8
    cost = [0]*(nodes+1)
    dist = [0]*(nodes+1)
    path = [0]*(stages+1)

    c = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 2, 1, 3, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 2, 3, 0, 0],
         [0, 0, 0, 0, 0, 6, 7, 0, 0],
         [0, 0, 0, 0, 0, 6, 8, 9, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 6],
         [0, 0, 0, 0, 0, 0, 0, 0, 4],
         [0, 0, 0, 0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    cost[nodes] = 0
    for i in range(nodes-1, -1, -1):
        mi = float("inf")
        for j in range(i+1, nodes+1):
            if c[i][j] != 0 and c[i][j]+cost[j] < mi:
                mi = c[i][j]+cost[j]
                dist[i] = j
        cost[i] = mi
    path[1] = 1
    path[stages] = nodes
    for i in range(2, stages):
        path[i] = dist[path[i-1]]

    print(path[1:nodes+1])
    return


if __name__ == "__main__":
    multistage_graph()
