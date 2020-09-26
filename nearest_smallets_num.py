# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/nearest-smaller-element/
Find smallest number.
"""

def solve(a):
    n = len(a)
    stack = []
    ans = []
    for k, v in enumerate(a):
        while stack and stack[-1] >= a[k]:
            stack.pop()
        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        stack.append(a[k])

    return ans[::]

if __name__ == "__main__":
    a = [(lambda x: int(x))(x) for x in input().split()]
    print(solve(a))
