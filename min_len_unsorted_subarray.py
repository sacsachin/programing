# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/maximum-unsorted-subarray/
Maximum Unsorted Subarray
"""

def solve(A):
    n = len(A)
    A = [(A[i], i) for i in range(n)]
    A.sort()
    #print(A)
    min_index = -1
    max_index = n
    for i in range(n):
        if A[i][1] != i:
            min_index = i
            break
    for i in range(n):
        if A[n-i-1][1] != n-i-1:
            max_index = n-i-1
            break
    if min_index == -1 and max_index == n:
        return -1
    return [min_index, max_index]

if __name__ == "__main__":
    A = [(lambda x: int(x))(x) for x in input().split(" ")]
    print(solve(A))
