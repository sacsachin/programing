# !/usr/bin/python3

"""
"""
def binary_search(a, n, ans):
    for index in range(n-2):
        lo = index+1
        hi = n-1
        while lo < hi:
          if a[index]+a[lo]+a[hi] == 0:
              ans.add((a[index], a[lo], a[hi]))
              lo += 1
              hi -= 1
          elif a[index]+a[lo]+a[hi] < 0:
              lo += 1
          else:
              hi -= 1
    return ans

def solve(a):
    n = len(a)
    a.sort()
    ans = set()
    ans = binary_search(a, n, ans)
    return list(ans)

if __name__ == "__main__":
    a = [(lambda x: int(x))(x) for x in input().split(" ")]
    print(set(solve(a)))
