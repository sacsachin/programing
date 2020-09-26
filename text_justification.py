# !/usr/bin/python3

"""
https://leetcode.com/problems/text-justification/
Text Justification.
"""

def arrange_space(a, start_idx, end_idx, spaces):
    word_cnt = end_idx-start_idx+1
    line = ""
    if word_cnt == 1:
        line += a[start_idx]
        line += " "*spaces
        return line
    evenly_dist = spaces//(word_cnt-1)
    extra_spaces = spaces%(word_cnt-1)
    for i in range(start_idx, end_idx+1):
        line += a[i]
        if end_idx == len(a)-1 and spaces > 0:
            line += " "
            spaces -= 1
            if i == end_idx:
                for i in range(spaces):
                    line += " "
        else:
            if i != end_idx:
                for i in range(evenly_dist):
                    line += " "
                if extra_spaces > 0:
                    line += " "
                    extra_spaces -= 1
    return line

def solve(a, w):
    n = len(a)
    ans = []
    i = 0
    while i < n:
        word_count = 0
        width = 0
        start_idx = i
        while i < n:
            width += len(a[i])
            word_count += 1
            if width+word_count-1 <= w:
                i += 1
            else:
                width -= len(a[i])
                word_count -= 1
                break
        end_idx = i-1
        line = arrange_space(a, start_idx, end_idx, w-width)
        ans.append(line)
    return ans

if __name__ == "__main__":
    a = input().split()
    w = int(input())
    ans = solve(a, w)
    for line in ans: print(line)
