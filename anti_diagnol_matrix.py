# !/usr/bin/python3


"""
https://www.interviewbit.com/problems/anti-diagonals/
Anti Diagnols
"""


def solve(A, n):
    for j in range(n):
        temp = j
        for i in range(j+1):
            print(A[i][temp], end="  ")
            temp-=1
        print(end="\n")

    for i in range(1, n):
        temp = i
        for j in range(n-1, i-1, -1):
            print(A[temp][j], end=" ")
            temp+=1
        print(end="\n")



if __name__ == "__main__":
    n = int(input())
    #c = int(input())
    A = [list(map(int, input().split(" "))) for i in range(n)]
    print(solve(A, n))
