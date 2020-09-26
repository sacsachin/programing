# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/evaluate-expression/
Evaluate expression.
"""

def solve(a):
    stack = []

    for c in a:
        if c == '+':
            stack.append(int(stack.pop())+int(stack.pop()))
        elif c == '-':
            value = int(stack.pop())
            stack.append(int(stack.pop())-value)
        elif c == '*':
            stack.append(int(stack.pop())*int(stack.pop()))
        elif c == '/':
            divisor = int(stack.pop())
            stack.append(int(stack.pop())//divisor)
        else:
            stack.append(c)
        # print(stack)

    return stack.pop()

if __name__ == "__main__":
    a = input().split()
    print(solve(a))
