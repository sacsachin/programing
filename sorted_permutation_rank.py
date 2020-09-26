# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/sorted-permutation-rank/
Sorted Permutaion Rank
"""
def fact(n, MOD):
    result = 1
    for i in range(2, n+1):
        result = (result*i) % MOD
    return result

def solve(A):
    MOD = 1000000 + 3
    index = 1
    first = list(A)
    first.sort()

    for each in A:
        pos = first.index(each)
        index = (index + (pos * fact((len(first)-1), MOD))) % MOD
        first.remove(each)
    return index % MOD

if __name__ == "__main__":
    A = input()
    print(solve(A))

