# !/usr/bin/python3

"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

def bisect_right(arr, target, lo=0, hi=None):
    index = -1
    if lo < 0:
        raise ValueError("lo must be non negetive")
    if hi == None:
        hi = len(arr)
    while lo < hi:
        mid = (lo+hi)//2
        if target < arr[mid]
            hi = mid
        else:
            if target == arr[mid]:
                index = mid
            lo = mid+1
    return index

def bisect_left(arr, target, lo=0, hi=None):
    index = -1
    if lo < 0:
        raise ValueError("lo must be non negative.")
    if hi == None:
        hi = len(arr)
    while lo < hi:
        mid = (lo+hi)//2
        if arr[mid] < target:
            lo = mid+1
        else:
            if target == arr[mid]:
                index = mid
            hi = mid
    return index

def solve(arr, target):
    ans = [0, 0]
    ans[0] = bisect_left(arr,target)
    ans[1] = bisect_right(arr, target)

    return ans

if __name__ == "__main__":
    arr = [(lambda x: int(x))(x) for x in input().split(" ")]
    target = int(input())
    print(solve(arr, target))
