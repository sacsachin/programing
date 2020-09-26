# !/usr/bin/python3

"""
"""

def binary_search(arr, target):
    n = len(arr)
    lo = 0
    hi = n-1

    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == target:
            return mid
        elif arr[lo] <= arr[mid]:
            if target >= arr[lo] and target <= arr[mid]:
                hi = mid-1
            else:
                lo = mid+1
        else:
            if target >= arr[mid] and target <= arr[hi]:
                lo = mid+1
            else:
                hi = mid-1
    return -1

def solve(arr, target):
    if not arr:
        return -1
    ans = binary_search(arr, target)

    return ans



if __name__ == "__main__":
    arr = list(map(int, input().split(", ")))
    target = int(input())
    print(solve(arr, target))
