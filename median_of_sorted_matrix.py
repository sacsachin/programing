# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/matrix-median/
Binary Search
"""

from bisect import bisect_right


def binary_search(matrix, mi, mx, m, n):
    target = (m*n+1)//2

    while mi < mx:
        mid = (mi+mx)//2
        less_then_mid = 0
        for i in range(m):
            less_then_mid += bisect_right(matrix[i], mid)
        if less_then_mid < target:
            mi = mid+1
        else:
            mx = mid

    return mi

def solve(matrix):
    m = len(matrix)
    n = len(matrix[0])

    mi = float("inf")
    mx = float("-inf")
    for i in range(m):
        if matrix[i][0] < mi:
            mi = matrix[i][0]
        if matrix[i][n-1] > mx:
            mx = matrix[i][n-1]
    # print(mi)
    # print(mx)

    ans = binary_search(matrix, mi, mx, m, n)

    return ans

if __name__ == "__main__":
    row = int(input())
    matrix = [[(lambda x: int(x))(x) for x in input().split(" ")] for _ in range(row)]
    print(solve(matrix))
