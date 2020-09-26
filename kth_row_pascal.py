# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/
kth row of pascal triangle.
"""

def pascal(n):
    ans = [1]
    for k in range(A):
        ans.appned(ans[k]*(n-k)//(k+1))
    return ans


if __name__ == "__main__":
    A = int(input())
    print(solve(A))
