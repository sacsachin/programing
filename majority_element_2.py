# !/usr/bin/python3

"""
Based on Moores voting algorithm.
"""

def solve(A):
    n = len(A)
    ans = []
    count1 = count2 = 0
    first = second = float("inf")

    for i in range(n):
        if A[i] ==  first:
            count1 += 1
        elif A[i] == second:
            count += 1
        elif count1 == 0:
            first = A[i]
            count1 = 1
        elif count2 == 0:
            second = A[i]
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    count1 = count2 = 0

    for i in range(n):
        if A[i] == first:
            count1 += 1
        elif A[i] == second:
            count2 += 1
    if count1 > n//3:
        ans.append(first)
    if count2 > n//3:
        ans.append(second)

    return ans

if __name__ == "__main__":
    A = [(lambda x: int(x))(x) for x in input().split(" ")]
    print(solve(A))
