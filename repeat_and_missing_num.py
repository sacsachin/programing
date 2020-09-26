# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/repeat-and-missing-number-array/
Repeat and Missing Number Array
"""
def solve(A):
    n = len(A)
    for i in range(n):
        if A[abs(A[i])-1] > 0:
            A[abs(A[i])-1] = -A[abs(A[i])-1]
        else:
            missing = abs(A[i])
    print(A)
    return [missing, A.index(max(A))+1]


if __name__ == "__main__":
    A = [(lambda x: int(x))(x) for x in input().split(", ")]
    print(solve(A))

