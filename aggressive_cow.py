# !/usr/bin/python3

"""
https://www.spoj.com/problems/AGGRCOW/
Aggressive Cow
"""

def valid_distance(a, n, c, mid):
    current_distance = 0
    current_cow = 1

    for i in range(1, n):
        current_distance += a[i]-a[i-1]
        if current_distance >= mid:
            current_cow += 1
            current_distance = 0
    return False if current_cow < c else True

def binary_search(a, n, c):
    lo = a[1]-a[0]
    hi = a[n-1]-a[0]
    ans = -1
    # lo = 0
    # hi = max(a)-lo

    while lo <= hi:
        mid = (lo+hi)//2
        if valid_distance(a, n, c, mid):
            lo = mid+1
            ans = mid
        else:
            hi = mid-1
    return ans

def solve(a, n, c):
    a.sort()
    if c == 2:
        return a[n-1]-a[0]
    return binary_search(a, n, c)

if __name__ == "__main__":
    t = int(input())
    while t:
        n, c = [(lambda x: int(x))(x) for x in input().split(" ")]
        stall = [0]*n
        temp = 0
        while temp < n:
            stall[temp] = int(input())
            temp += 1
        print(solve(stall, n, c))
        t -= 1

