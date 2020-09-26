# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/max-non-negative-subarray/
Max Non Negative Subarray
"""


def solve(A):
    n = len(A)
    start = 0
    end = 0
    max_sum = temp_sum = 0
    max_len = temp_len = 0
    ans = []

    for i in range(n):
        if A[i] >= 0:
            temp_sum += A[i]
            temp_len += 1
            end +=1
        if A[i] < 0 or i == n-1:
            if temp_sum > max_sum:
                ans = A[start:end]
                max_sum = temp_sum
                max_len = temp_len
            elif temp_sum == max_sum and temp_len > max_len:
                ans = A[start:end]
                max_len = temp_len
            temp_len = temp_sum = 0
            start = i+1
            end += 1
    return ans

if __name__ == "__main__":
    A = [(lambda x: int(x))(x) for x in input().split(" ")]
    print(solve(A))
