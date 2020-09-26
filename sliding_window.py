# !/usr/bin/python3

"""
https://leetcode.com/problems/sliding-window-maximum/
Sliding window maximum.
"""

def heapify(a, start, end):
    for i in range(end, start-1, -1):
        if i*2+1 <= end:
            j = i*2 if a[i*2] > a[i*2+1] else i*2+1
        elif i*2 <= end:
            j = i*2
        else:
            continue
        if a[j] > a[i]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
    return

def solve(a, k):
    n = len(a)
    ans = []
    start = 0
    end = k-1
    while end < n:
        heap = [0]+a[start:end+1]
        heapify(heap, 1, k)
        print(heap)
        ans.append(heap[1])
        start += 1
        end += 1

    return ans[::]

if __name__ == "__main__":
    a = list(map(int, input().split()))
    k = int(input())
    print(solve(a, k))
