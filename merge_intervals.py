# !/usr/bin/python3

"""
"""

def solve(A, B):
    if not A:
        return B
    A += [B]
    n = len(A)
    # print(A)
    A.sort(key=lambda x: x[0])
    print(A)
    ans = [A[0]]
    for i in range(1, n):
        if A[i][0] <= ans[len(ans)-1][1]:
            ans[len(ans)-1][1] = max(A[i][1], ans[len(ans)-1][1])
        else:
            ans.append(A[i])

    return ans


if __name__ == "__main__":
    n = int(input())
    A = [[(lambda x: int(x))(x) for x in input().split(" ")] for _ in range(n)]
    B =[(lambda x: int(x))(x) for x in input().split(" ")]
    # print(A)
    # print(B)

    print(solve(A, B))
