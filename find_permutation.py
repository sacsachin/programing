# !/usr/bin/python3

"""
"""

def solve(A):
    n = len(A)
    stack = []
    ans = []

    for i in range(1, n+1):
        if A[i-1] == "D":
            stack.append(i)
        else:
            stack.append(i)
            while stack:
                ans.append(stack.pop())

    stack.append(n+1)
    while stack:
        ans.append(stack.pop())

    return ans


if __name__ == "__main__":
    A = input()
    print(solve(A))
