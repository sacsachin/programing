# !/usr/bin/pyhton3

"""
https://www.interviewbit.com/problems/merge-overlapping-intervals/
"""

def solve(A, n):
    n = len(A)
    A.sort(key=lambda x: x[0])

    ans = [A[0]]
    # count = 1
    for i in range(1, n):
        if A[i][1] <= ans[len(ans)-1][1]:
            continue
        elif A[i][0] <= ans[count-1][1]:
            ans[len(ans)-1][1] = A[i][1]
        else:
            ans.append(A[i])
            #count += 1

    return ans

if __name__ == "__main__":
    n = int(input())
    A = [list(map(int, input().split(" "))) for _ in range(n)]
    #A = [(lambda x, y: (int(x), int(y)))() for _ in range(n)]
    print(solve(A, n))
