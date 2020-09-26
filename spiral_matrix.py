# !/usr/bin/python3

"""
"""

def solve(matrix, n):
    #matrix = [[None  for _ in range(A)] for _ in range(A)]
    t = n*n
    count = 0
    i = j = 0
    while t is not 0:
        for a in range(j, n-count, 1):
            print(matrix[i][a], end=" ")
            j=a
            t-=1
        i+=1
        for a in range(i, n-count, 1):
            print(matrix[a][j], end=" ")
            i=a
            t-=1
        j-=1
        for a in range(j, count-1, -1):
            print(matrix[i][a], end=" ")
            j=a
            t-=1
        i-=1
        for a in range(i, count, -1):
            print(matrix[a][j], end=" ")
            i=a
            t-=1
        j+=1
        count += 1
    return matrix


if __name__ == "__main__":
    n = int(input())
    matrix = [[(lambda x: int(x))(x) for x in input().split(" ")] for _ in range(n)]
    print(solve(matrix, n))
