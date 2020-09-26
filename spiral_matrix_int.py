# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/spiral-order-matrix-ii/
Spiral Matrix of square.
"""

def solve(n):
    matrix = [[None  for _ in range(n)] for _ in range(n)]
    t = n*n
    number = 1
    count = 0
    i = j = 0
    while t is not 0:
        for a in range(j, n-count, 1):
            #print(matrix[i][a], end=" ")
            matrix[i][a] = number
            number+=1
            j=a
            t-=1
        i+=1
        for a in range(i, n-count, 1):
            #print(matrix[a][j], end=" ")
            matrix[a][j] = number
            number+=1
            i=a
            t-=1
        j-=1
        for a in range(j, count-1, -1):
            #print(matrix[i][a], end=" ")
            matrix[i][a] = number
            number+=1
            j=a
            t-=1
        i-=1
        for a in range(i, count, -1):
            #print(matrix[a][j], end=" ")
            matrix[a][j] = number
            number+=1
            i=a
            t-=1
        j+=1
        count += 1
    for each in matrix:
        print(each)
    return matrix


if __name__ == "__main__":
    n = int(input())
    #matrix = [[(lambda x: int(x))(x) for x in input().split(" ")] for _ in range(n)]
    print(solve(n))
