# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/allocate-books/
Allocat Book
Binary search
"""
def valid_configuration(a, n , mid, students):
    current_students = 1
    current_page = 0
    for i in range(n):
        if current_page+a[i] <= mid:
            current_page += a[i]
        else:
            current_students += 1
            current_page = a[i]
            if current_students > students:
                return False

    # return True if current_students == students else False
    return True

def binary_search(a, n , lo , hi, students):
    valid_ans = 0
    while lo <= hi:
        mid = (lo+hi)//2
        if valid_configuration(a, n , mid, students):
            valid_ans = mid
            hi = mid-1
        else:
            lo = mid+1
    return valid_ans

def solve(arr, students):
    n = len(arr)
    if not arr or not students:
        return -1
    if n < students:
        return -1
    lo = 0
    hi = 0
    for i in range(n):
        if arr[i] > lo:
            lo = arr[i]
        hi += arr[i]
    ans = binary_search(arr, n, lo, hi, students)

    return ans

if __name__ == "__main__":
    arr = [(lambda x: int(x))(x) for x in input().split(" ")]
    students = int(input())
    print(solve(arr, students))
