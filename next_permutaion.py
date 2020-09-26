# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/next-permutation/
Next Permutation

Binary Search
Swaping
"""

def swap(A, index1, index2):
    temp = A[index1]
    A[index1] = A[index2]
    A[index2] =temp

    return A

def binary_search(A, start, end, val):
    index = -1
    while start <= end:
        mid = start+(end-start)//2
        if A[mid] <= val:
            end = mid-1
        else:
            start = mid+1
            if index == -1 or A[index] >= A[mid]:
                index = mid

    return index

def solve(A):
    n = len(A)
    A = list(A)
    i = n-2
    while i >= 0 and A[i] >= A[i+1]:
        i -= 1

    if i < 0:
        return A[::-1]
    else:
        index = binary_search(A, i+1, n-1, A[i])
        A = swap(A, i, index)
        first = A[0:i+1]
        second = A[i+1:n]
        second = second[::-1]
        A = first+second

    return A

if __name__ == "__main__":
    A = input()
    print("".join(solve(A)))
