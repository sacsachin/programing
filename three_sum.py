# !/usr/bin/python3

def helper(a, n, val):
    ans = 0
    least_diff = float("inf")
    for i in range(n-1, 1, -1):
        lo = 0
        hi = i-1
        while lo < hi:
            if a[i]+a[lo]+a[hi] == val:
                return val
            elif a[i]+a[lo]+a[hi] > val:
                diff = a[i]+a[lo]+a[hi] - val
                if diff < least_diff:
                    least_diff = diff
                    ans = a[i]+a[lo]+a[hi]
                hi -= 1
            else:
                diff = val-(a[i]+a[lo]+a[hi])
                if diff < least_diff:
                    least_diff = diff
                    ans = a[i]+a[lo]+a[hi]
                lo += 1
    return ans

def solve(a, k):
    n = len(A)
    A.sort()
    ans = 0
    ans = helper(A, n, B)
    return ans

if __name__ == "__main__":
    a = [(lambda x: int(x))(x) for  x in input().split()]
    k = int(input())
    print(solve(a, k))
