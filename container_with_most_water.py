# !/usr/bin/python3

"""
"""

def solve(A):
    n = len(A)
    start = 0
    end = n-1
    ans = 0
    while start < end:
        ans = max(ans, min(A[start], A[end])*(end-start))
        if A[start] < A[end]:
            start += 1
        else:
            end -= 1
    return ans
if __name__ == "__main__":
    A = [(lambda x: int(x))(x) for x in input().split()]
    print(solve(A))
