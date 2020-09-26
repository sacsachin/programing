# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/add-one-to-number/
Add 1 to Number
"""

def solve(A):
    # fact = 1
    # num = 0
    # B = []
    # for i in range(len(A)-1, -1, -1):
        # num+=A[i]*fact
        # fact *=10
    # num +=1

    # while num:
        # B.append(num%10)
        # num //=10
    # return B[::-1]
    carry = 1
    for i in range(len(A)-1, -1, -1):
        if A[i]==9:
            A[i] =0
            carry = 1
        else:
            A[i] = A[i]+1
            carry = 0
            break
    if carry:
        return [1] + A
    ind = -1
    for i in range(0, len(A)):
        if A[i] is not 0:
            ind = i
            break
    return A[ind:]

if __name__ == "__main__":
    A = list(map(int, input().split(" ")))
    print(solve(A))
