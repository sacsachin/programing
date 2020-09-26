# !/usr/bin/python3

"""
Two Sum.
https://leetcode.com/problems/two-sum/
"""

def solve(a, k):
    n = len(a)
    hash_map = dict()

    for index, val in enumerate(a):
        if val in hash_map: hash_map[val].append(index)
        else: hash_map.setdefault(val, [index])

    print(hash_map)
    for key, val in hash_map.items():
        remaining = k-key
        if remaining in hash_map:
            if remaining == key and len(val) == 2: return (val[0], val[1])
            elif remaining != key: return (val[0], hash_map[remaining][0])
    return

if __name__ == "__main__":
    a = list(map(int, input().split(", ")))
    k = int(input())
    print(solve(a, k))
