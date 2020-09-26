# !/usr/bin/python3

"""
"""

def valid_assignment(a, n, mid, p):
    current_p = 1
    current_board = 0
    for i in range(n):
        if current_board+a[i] <= mid:
            current_board += a[i]
        else:
            current_p += 1
            current_board = a[i]
            if current_p > p:
                return False
    return True

def binary_search(a, n, lo, hi, p):
    final_ans = 0
    while lo <= hi:
        mid = (lo+hi)//2
        if valid_assignment(a, n, mid, p):
            hi = mid-1
            final_ans = mid
        else:
            lo = mid+1
    return final_ans

def solve(a, p):
    n = len(a)
    if not n or not p:
        return -1
    lo = 0
    hi = 0

    for i in range(n):
        if a[i] > lo:
            lo = a[i]
        hi += a[i]
    if p >= n:
        return lo
    return binary_search(a, n, lo, hi, p)

if __name__ == "__main__":
    boards = [(lambda x: int(x))(x) for x in input().split(" ")]
    painters = int(input())
    print(solve(boards, painters))
