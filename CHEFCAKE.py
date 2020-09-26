# !/usr/bin/python3

"""
https://www.codechef.com/QFUN2020/problems/CHEFCAKE
Chef and cakes.
"""

def solve():
    ans = 0
    pow_10 = 10**(n-1)

    fac_n = 1
    for i in range(1, n+1):
        fac_n *= i

    each_occ = fac_n//n
    while pow_10:
        for  digit in a:
            ans += digit*pow_10*each_occ
        pow_10 //= 10
    return ans

if __name__ == "__main__":
    t = int(input())
    while t:
        n = int(input())
        a = input().split()
        # print(a)
        a = [int(num) for num in a]
        t -= 1
        print(solve())

