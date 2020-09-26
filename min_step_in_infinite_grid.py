# ! /usr/bin/python3

"""
https://www.interviewbit.com/problems/min-steps-in-infinite-grid/
Min Step In Grid.
"""

def solve(A, B):
    ans = 0
    for i in range(1, len(A)):
        if abs(A[i]-A[i-1]) == abs(B[i]-B[i-1]):
            ans+=abs(A[i] - A[i-1])
        elif abs(A[i]-A[i-1]) > abs(B[i]-B[i-1]):
            ans+=abs(A[i]-A[i-1])
        else:
            ans+=abs(B[i]-B[i-1])
    return ans

if __name__ == "__main__":
    A = list(map(int, input().split(" ")))
    B = list(map(int, input().split(" ")))

    print(solve(A, B))

