# !/usr/bin/python3


def binary_search(a, i, j, n):
    ans = j
    lo = j+1
    hi = n-1
    while lo <= hi:
        mid = (lo+hi)//2
        if a[i]+a[j] > a[mid]:
            ans = mid
            lo = mid+1
        else:
            hi = mid-1
    return ans -j

def solve(a):
    n = len(a)
    a.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            ans += binary_search(a, i, j, n)
    return ans

if __name__ == "__main__":
    a = [(lambda x: int(x))(x) for x in input().split()]
    print(solve(a))
