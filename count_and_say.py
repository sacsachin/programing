# !/usr/bin/python3


def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 11
    curr = "11"

    for i in range(2, n):
        prv = curr
        curr = ""
        prv_len = prv.__len__()
        count = 1
        for j in range(1, prv_len):
            if prv[j-1] == prv[j]:
                count += 1
            else:
                curr += str(count)+prv[j-1]
                count = 1
        curr += str(count)+prv[prv_len-1]
    return curr

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
