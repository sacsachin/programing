# !/usr/bin/python3

"""
Sliding window problem
"""

def sliding_window(a, n, k):
    wl = wr = 0
    zero_count = 0
    best_l = best_win_s = 0

    while wr < n:
        if zero_count <= k:
            if a[wr] == 0:
                zero_count += 1
            wr += 1
        if zero_count > k:
            if a[wl] == 0:
                zero_count -= 1
            wl += 1
        if wr-wl > best_win_s:
            best_win_s = wr-wl
            best_l = wl
    ans = []
    print(best_win_s)
    print(best_l)
    for i in range(best_win_s):
        if a[best_l+i] == 0:
            ans.append(best_l+i)
    return ans

def solve(a, k):
    n = a.__len__()
    ans = sliding_window(a, n, k)
    return ans

if __name__ == "__main__":
    a = [(lambda x: int(x))(x) for x in input().split(" ")]
    k = int(input())
    print(solve(a, k))
