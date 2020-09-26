# /usr/bin/python3

def binary_search(a, lo, hi, val):
    index = lo-1
    while lo <= hi:
        mid = (lo+hi)//2
        if a[mid]-a[index] == val:
            return [a[index], a[mid]]
        elif a[mid]-a[index] > val:
            hi = mid-1
        else:
            lo = mid+1
    return []

def solve(a, k):
    n = len(a)
    ans = 0
    a.sort()
    pair = [float("inf"), float("inf")]
    for i in range(n-1):
        temp = binary_search(a, i+1, n-1, k)
        if temp and temp != pair:
            ans += 1
            pair = temp

    return ans


if __name__ == "__main__":
    a = [(lambda x: int(x))(x) for x in input().split()]
    k = int(input())
    print(solve(a, k))
