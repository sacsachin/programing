# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/set-matrix-zeros/
Set Matrix Zeroes
"""

def solve(A, m, n):
    first_row = first_col = False

    for j in range(n):
        if A[0][j] is 0:
            first_row = True
            break
    for  i in range(m):
        if A[i][0] is 0:
            first_col = True
            break

    for i in range(1, m):
        for j in range(1, n):
            if A[i][j] is 0:
                A[0][j] = 0
                A[i][0] = 0

    for i in range(1, m):
        for j in range(1, n):
            if A[i][0] is 0 or A[0][j] is 0:
                A[i][j] = 0

    if first_row:
        for j in range(n):
            A[0][j] = 0
    if first_col:
        for i in range(m):
            A[i][0] = 0

    return A
if __name__ == "__main__":
    m = int(input())
    n = int(input())
    A = [[(lambda x: int(x))(x) for x in input().split(" ")] for _ in range(m)]
    print(solve(A, m, n))
