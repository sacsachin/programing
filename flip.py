# !/usr/bin/python

"""
https://www.interviewbit.com/problems/flip/
Flip
Kadane's algo
"""

def solve(A):
    diff = 0
    max_diff = 0
    start = 0
    ans = None

    for i, a in enumerate(A):
        diff += 1 if a is '0' else -1

        if diff < 0:
            diff = 0
            start = i+1

        if diff > max_diff:
            max_diff = diff
            ans = [start, i]

    if ans is None:
        return []
    return list(map(lambda x: x+1, ans))


if __name__ == "__main__":
    A = input()
    print(solve(A))
