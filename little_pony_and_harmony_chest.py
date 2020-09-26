# !/usr/bin/python3

dp[101][16] = [[-1 for _ in range(16)] for _ in range(101)]
b[101][16] = [[-1 for _ in range(16)] for _ in range(101)]
p = [2, 3, 5, 7, 11, 13 , 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]


def solve(n, a):
    factormask = [0 for _ in range(59)]
    for i in range(1, 59):
        for j in range(16):
            if i%p[j] == 0:
                factormask |= (1<<j)
    fullmask = (1<<16)-1
    calc(n, fullmask)
    b_out = []
    mask = fullmask
    for i in range(n, -1, -1):
        curr = b[i][mask]







if __name__ == "__main__":
    n = int(input())
    a = [(lambda x: int(x))(x) for x in input().split()]
    print(solve(n, a))
