# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/simplify-directory-path/
Simplify directory path.
"""

def solve(s):
    stack = []

    s = s.lstrip().rstrip().split("/")
    for each in s:
        if each == "..":
            if stack: stack.pop()
        elif each == ".":
            continue
        elif each:
            stack.append(each)

    return "/"+"/".join(stack)

if __name__ == "__main__":
    s = input()
    print(solve(s))
