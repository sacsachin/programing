# !/usr/bin/python3


def binary_search(X, Y):
    if len(X) > len(Y):
        return binary_search(Y, X)
    m = len(X)
    n = len(Y)

    start = 0
    end = m

    while start <= end:
        mid_x = (start+end)//2
        mid_y = (m+n+1)//2-mid_x

        max_left_x = float("-inf") if mid_x == 0 else X[mid_x-1]
        min_right_x = float("inf") if mid_x == m else X[mid_x]

        max_left_y = float("-inf") if mid_y == 0 else Y[mid_y-1]
        min_right_y = float("inf") if mid_y == n else Y[mid_y]

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (m+n)%2 == 0:
                return (max(max_left_x, max_left_y)+min(min_right_x, min_right_y))/2
            else:
                return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            end = mid_x-1
        else:
            start = mid_x+1

    raise ValueError("Bad Argument")


if __name__ == "__main__":
    A = [(lambda x: int(x))(x) for x in input().split(" ")]
    B = [(lambda x: int(x))(x) for x in input().split(" ")]

    print(binary_search(A, B))
