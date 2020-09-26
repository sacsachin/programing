# !/use/bin/python3

"""
https://atcoder.jp/contests/abc151/tasks/abc151_a
Next Alphabate
"""

def solve(c):
    ans = ord(c)
    return chr(ans+1)

if __name__ == "__main__":
    c = input()
    print(solve(c))
