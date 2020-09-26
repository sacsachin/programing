# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/largest-continuous-sequence-zero-sum/
Largest contineous zero sum array.
"""

def solve(a):
    n = len(a)
    max_len = 0
    current_sum = 0
    hash_map = dict()

    for index, val in enumerate(a):
        current_sum += val

        # if a[index] == 0 and max_len == 0:
            # max_len = 1
        if current_sum == 0:
            max_len = index+1
        if current_sum in hash_map:
            max_len = max(max_len, index-hash_map.get(current_sum))
        else:
            hash_map.setdefault(current_sum, index)
    return max_len

if __name__ == "__main__":
    a = [(lambda x: int(x))(x) for x in input().split()]
    print(solve(a))
