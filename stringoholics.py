# !/usr/bin/python3

"""
Stringoholics
https://www.interviewbit.com/problems/stringoholics
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def solve(a):
    MOD = 1000000000+7
    n = len(a)
    t = [0 for _ in range(n)]
    for i in range(n):
        if len(set(a[i])) == 1:
            t[i] = 1
    for i in range(n):
        k = 1
        while True:
            if t[i] == 1:
                break
            elif (k*(k+1)//2)%len(a[i]) == 0:
                t[i] = k%MOD
                break
            k += 1
    ans = 1
    for i in range(n):
        ans = ans//gcd(ans, t[i])*t[i]
    return ans%MOD


if __name__ == "__main__":
    a = input().split()
    print(solve(a))
