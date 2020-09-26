# !/usr/bin/python3

def solve(n):
    r_dic = {1000: "M",
             900: "CM",
             500: "D",
             400: "CD",
             100: "C",
             90: "XC",
             50: "L",
             40: "XL",
             10: "X",
             9: "IX",
             5: "V",
             4: "IV",
             1: "I"
             }
    l = len(r_dic)
    ans = ""
    for k, v in r_dic.items():
        while n >= k:
            ans += v
            n -= k
    return ans

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
