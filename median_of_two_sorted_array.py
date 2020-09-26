# !/usr/bin/python3

"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

def solve(A, B):
    n = len(A)
    m = len(B)
    R = []

    i = j = 0
    while i < n and j < m:
        if A[i] <= B[j]:
            R.append(A[i])
            i += 1
        else:
            R.append(B[j])
            j += 1
    while i < n:
        R.append(A[i])
        i += 1
    while j < m:
        R.append(B[j])
        j += 1

    print(R)

    if len(R) % 2 == 0:
        return (R[len(R)//2]+R[len(R)//2-1])/2
    else:
        return R[len(R)//2]

if __name__ == "__main__":
    # row = int(input())
    A = [(lambda x: int(x))(x) for x in input().split(" ")]
    B = [(lambda x: int(x))(x) for x in input().split(" ")]

    print(solve(A, B))
