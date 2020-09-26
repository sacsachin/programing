# !/usr/bin/python3

def binary_search(x):
    if x < 2:
        return x
    start = 0
    end = x
    result = 1

    while start <= end:
        mid = (start+end)/2
        if mid*mid == x:
            return mid
        elif mid*mid < x:
            result = mid
            start = mid
        else:
            end = mid
    return result


def solve(x):
    return binary_search(x)

if __name__ == "__main__":
    x = int(input())
    print(solve(x))
