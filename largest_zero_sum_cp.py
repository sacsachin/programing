
# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/largest-continuous-sequence-zero-sum/
Largest contineous zero sum array.
"""

def solve(A):
    n = len(A)
    max_len = 0
    start = 0
    end = -1
    current_sum = 0
    hash_map = dict()

    for index, val in enumerate(A):
        current_sum += val

        # if a[index] == 0 and max_len == 0:
            # max_len = 1
        if current_sum == 0:
            max_len = index+1
            start = 0
            end = index+1
        if current_sum in hash_map:
            if index-hash_map.get(current_sum) > max_len:
                max_len = index-hash_map.get(current_sum)
                start = hash_map.get(current_sum)+1
                end = index
        else:
            hash_map.setdefault(current_sum, index)

    return A[start: end+1]
if __name__ == "__main__":
    a = [(lambda x: int(x))(x) for x in input().split()]
    print(solve(a))
