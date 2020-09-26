# /usr/bin/python3

"""
https://www.interviewbit.com/problems/sorted-permutation-rank-with-repeats/
Sorted permutation rank with repeat.
"""
def fact(n ,MOD):
    result = 1:
    for i in range(2, n+1):
        result = (result*i) % MOD
    return result

def solve(A):
    MOD = 1000000 + 3

if __name__ == '__main__':
    A  = input()
    print(solve(A))
