# !/usr/bin/python3

def solve(a):
    ans = 0
    n = len(a)
    for i in range(64):
        one = 0
        for j in range(n):
            one += a[j]&1
            a[j] >>= 1
        ans += one*(n-one)
    return ans*2

if __name__ == "__main__":
    arr = [(lambda x: int(x))(x) for x in input().split(" ")]
    print(solve(arr))
