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
    # diff = 0
    ans = float("inf")
    # ans = float()
    while i < m and j < n and k < p:
        mx = max(A[i], B[j], C[k])
        mi = min(A[i], B[j], C[k])
        ans = min(mx-mi, ans)

        if mi == A[i]:
            i += 1
        elif mi == B[j]:
            j += 1
        else:
            k += 1
    return ans

if __name__ == "__main__":
    A = [(lambda x: int(x))(x) for x in input().split()]
    B = [(lambda x: int(x))(x) for x in input().split()]
    C = [(lambda x: int(x))(x) for x in input().split()]
    print(solve(A, B, C))
