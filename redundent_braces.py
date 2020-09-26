# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/redundant-braces/
Redundent Braces.
"""
def solve(s):
    stack = []

    for c in s:
        # print(stack)
        if c == ')':
            if stack.pop() == '(' or stack.pop() == '(':
                return 1
            while stack:
                if stack.pop() == '(':
                    break
        else:
            stack.append(c)
    return 0

if __name__ == "__main__":
    s = input()
    print(solve(s))
