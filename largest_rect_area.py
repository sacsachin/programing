# !/usr/bin/python3

"""
"""

def solve(a):
    n = len(a)
    ans = current = 0
    stack = []

    while current <= n:
        while stack and (current == n or a[current] < a[stack[-1]]):
            top = stack.pop()
            if not stack:
                ans = max(ans, a[top]*current)
            else:
                ans = max(ans, a[top]*(current-stack[-1]-1))
        stack.append(current)
        current += 1

    return ans

if __name__ == "__main__":
    a = [(lambda x: int(x))(x) for x in input().split()]
    print(solve(a))
