# !/usr/bin/python3

"""
https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
Find duplicates in O(n) time and O(1) extra space
"""

def solve(A):
    ans = []
    n = len(A)
    for i in range(n):
        if A[i] == 0:
            A[i] = n
    for i in range(n):
        if A[abs(A[i])%n] > 0:
            A[abs(A[i])%n] = -A[abs(A[i])%n]
        else:
            if abs(A[i])%n not in ans:
                ans.append(abs(A[i])%n)
    return ans


if __name__ == "__main__":
    A = [(lambda x: int(x))(x) for x in input().split(" ")]
    print(solve(A))
