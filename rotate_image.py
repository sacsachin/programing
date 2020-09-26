# !/usr/bin/python3


def solve(A, n):
    itr = 0
    while itr < n//2:
        row = itr
        col = n-itr-1
        for k in range(itr, n-itr-1):
            temp = A[k][col]
            A[k][col] = A[row][k]

            temp1 = A[n-row-1][n-k-1]
            A[n-row-1][n-k-1] = temp

            temp = A[n-k-1][row]
            A[n-k-1][row] = temp1

            A[row][k] = temp

        itr += 1

    for each in A:
        print(each)

    return A


if  __name__ == "__main__":
    n = int(input())
    A = [[(lambda x: int(x))(x) for x in input().split(" ")] for _ in range(n)]
    print(solve(A, n))
