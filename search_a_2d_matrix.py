# !/usr/bin.python3

"""
https://leetcode.com/problems/search-a-2d-matrix/
Binary Search
"""

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            end = mid-1
        else:
            start = mid+1

    return False

def solve(A, B):
    m = len(A)
    n = len(A[0])

    ans = False

    for i in range(m):
        if B >= A[i][0] and B <= A[i][n-1]:
            ans = binary_search(A[i], B, 0, n-1)

    return ans

if __name__ == "__main__":
    row = int(input())
    target = int(input())
    A = [[(lambda x: int(x))(x) for x in input().split(" ")] for _ in range(row)]
    print(A)
    print(solve(A, target))
