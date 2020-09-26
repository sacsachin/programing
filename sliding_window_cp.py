# !/usr/bin/python3

"""
https://leetcode.com/problems/sliding-window-maximum/
Sliding window maximum.
"""

from collections import deque

def solve(a, k):
    ans = []
    dq = deque()
    for i, num in enumerate(a):
        while dq and a[dq[-1]] < num:
            dq.pop()
        if dq and i-dq[0] >=k:
            dq.popleft()
        dq.append(i)
        if i>= k-1: ans.append(a[dq[0]])
    return ans[::]

if __name__ == "__main__":
    a = list(map(int, input().split()))
    k = int(input())
    print(solve(a, k))
