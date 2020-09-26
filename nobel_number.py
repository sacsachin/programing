# !/usr/bin/python3

"""
"""

def solve(A):
    MIN = float("-inf")
    #A = set(A)
    A.sort()
    n = len(A)
    ans = []
    for i in range(n-1):
        if A[i] is A[i+1]:
            continue
        elif abs(A[i]) is (n-i-1):
            ans.append(A[i])

    return ans


if __name__ == "__main__":
    A = list(map(int, input().split(" ")))
    print(solve(A))
