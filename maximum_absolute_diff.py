# !/usr/bin/pcython3

"""
https://www.interviewbit.com/problems/maximum-absolute-difference/
Maximum Absolute Difference
Math
"""

def solve(A):
    n = len(A)
    B = [A[i]+i for i in range(n)]
    D = [A[i]-i for i in range(n)]
    return max(max(B)-min(B), max(D)-min(D))

if __name__ == "__main__":
    #A = list(map(lambda x: int(x), input().split(" ")))
    #f = lambda x: int(x)
    A = [(lambda x: int(x))(x) for x in input().split(" ")]
    print(solve(A))
