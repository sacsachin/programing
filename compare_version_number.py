# !/usr/bin/python3

def solve(s1, s2):
    s1 = s1.strip().split(".")
    s2 = s2.strip().split(".")
    s1 = [(lambda x: int(x))(x) for x in s1]
    s2 = [(lambda x: int(x))(x) for x in s2]
    n = s1.__len__()
    m = s2.__len__()
    i = j =0

    while i < n and j < m:
        if s1[i] > s2[j]:
            return 1
        elif s1[i] < s2[j]:
            return -1
        else:
            i += 1
            j += 1
    while i < n:
        if s1[i] > 0:
            return 1
        i += 1
    while j < m:
        if s2[j] > 0:
            return -1
        j += 1
    return 0

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(solve(s1, s2))
