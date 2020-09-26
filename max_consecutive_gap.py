# !/usr/bin/python3


def solve(A):
    n = len(A)
    if n == 1:
        return 0
    INT_MAX = float("inf")
    INT_MIN = float("-inf")

    max_val = max(A)
    min_val = min(A)

    max_arr = [INT_MIN]*(n)
    min_arr = [INT_MAX]*(n)

    delta = (max_val-min_val)//(n-1)
    # print(n)
    # print(max_val)
    # print(min_val)
    # print(delta)
    for i in range(n):
        if A[i] in (min_val, max_val):
            continue
        index = (A[i]-min_val)//delta
        if max_arr[index] == INT_MIN:
            max_arr[index] = A[i]
        else:
            max_arr[index] = max(max_arr[index], A[i])

        if min_arr[index] == INT_MAX:
            min_arr[index] = A[i]
        else:
            min_arr[index] = min(min_arr[index], A[i])

    prev_val, max_gap = (min_val, 0)
    # print(min_arr)
    # print(max_arr)
    for i in range(n):
        if min_arr[i] == INT_MAX:
            continue
        max_gap = max(max_gap, min_arr[i]-prev_val)
        prev_val = max_arr[i]
    max_gap = max(max_gap, max_val-prev_val)

    return max_gap


if __name__ == "__main__":
    A = [(lambda x: int(x))(x) for x in input().split(" ")]
    print(solve(A))
