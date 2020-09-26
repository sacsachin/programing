# !/usr/bin/python3

def solve(s):
    n = len(s)
    ans = 0
    d_map = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}
    for i in range(1, n):
        if d_map[s[i-1]] < d_map[s[i]]:
            ans -= d_map[s[i-1]]
        else:
            ans += d_map[s[i-1]]
    ans += d_map[s[n-1]]

    return ans

if __name__ == "__main__":
    s = input()
    print(solve(s))
