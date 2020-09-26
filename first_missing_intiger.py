# !/usr/bin/python

"""
https://www.interviewbit.com/problems/first-missing-integer/
First Missing Number
"""

def solve(A):
    n = len(A)
    MAX = float("inf")
    MIN = float("-inf")
    for i in range(n):
        if A[i] <= 0 or A[i] > n:
            A[i] = MAX
    for i in range(n):
        if A[i] in (MAX, MIN):
            continue
        if A[abs(A[i])-1] > 0:
            A[abs(A[i])-1] = -A[abs(A[i])-1]

    for i in range(n):
        if A[i] > 0:
            return i+1
    return n+1

if __name__ == "__main__":
    A = [(lambda x: int(x))(x) for x in input().split(" ")]
    print(solve(A))
