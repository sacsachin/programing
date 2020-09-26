# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/minimize-the-absolute-difference/
Minimize the absolute difference
"""

def solve(A, B, C):
    m = len(A)
    n = len(B)
    p = len(C)

    i = j = k = 0
    diff = float("inf")
    a_i = b_j = c_k = 0
    while i < m and j < n and k < p:
        mx = max(A[i], B[j], C[k])
        mi = min(A[i], B[j], C[k])
        if mx-mi < diff:
            diff = mx-mi
            a_i = i
            b_j = j
            c_k = k

        if mi == A[i]:
            i += 1
        elif mi == B[j]:
            j += 1
        else:
            k += 1
    return [A[a_i], B[b_j], C[c_k]]

if __name__ == "__main__":
    A = [(lambda x: int(x))(x) for x in input().split()]
    B = [(lambda x: int(x))(x) for x in input().split()]
    C = [(lambda x: int(x))(x) for x in input().split()]
    print(solve(A, B, C))
