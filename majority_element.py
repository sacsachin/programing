# !/usr/bin/python3

"""
Moores Voting algorithm.
Majority element in a array.
"""

def solve(A):
    n = len(A)
    index = 0
    count = 1

    for i in range(1, n):
        if A[index] is A[i]:
            count +=1
        else:
            count -=1

        if count is 0:
            index = i
            count = 1

    count = 0
    for i in range(n):
        if A[i] is A[index]:
            count +=1

    return (A[index], count)

if __name__ == "__main__":
    A = list(map(int, input().split(" ")))
    print(solve(A))
