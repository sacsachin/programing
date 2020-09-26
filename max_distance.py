# !/usr/bin/python3
"""
Max diffrence
https://www.interviewbit.com/problems/max-distance/
"""
def solve(A):
    n = len(A)
    A = [(A[i], i) for i in range(n)]
    A.sort()
    #print(sorted(A, key=lambda x: (x[0])))
    temp_diff = n
    max_diff = 0
    for i in range(n):
        if temp_diff > A[i][1]:
            temp_diff = A[i][1]
        max_diff = max(max_diff, A[i][1]-temp_diff)

    return max_diff if max_diff > 0 else -1


if __name__ == "__main__":
    A = [(lambda x: int(x))(x) for x in input().split(" ")]
    print(solve(A))
