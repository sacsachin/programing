# !/usr/bin/python3

"""
Add Binary Strings
https://www.interviewbit.com/problems/add-binary-strings/
"""

def add_binary(s1, s2):
    n = len(s1)
    m = len(s2)
    i = n-1
    j = m-1
    carry = 0
    res = ""
    while i >= 0 and j >= 0:
        if s1[i] == '1' and s2[j] == '1':
            if carry == 1:
                res = '1'+res
            else:
                res = '0'+res
            carry = 1
        elif s1[i] == '1' or s2[j] == '1':
            if carry == 1:
                res = '0'+res
                carry = 1
            else:
                res = '1'+res
        else:
            if carry == 1:
                res = '1'+res
                carry = 0
            else:
                res = '0'+res
        i -= 1
        j -= 1
    while i >= 0:
        if carry == 1 and s1[i] == '1':
            res = '0'+res
            carry = 1
        elif carry == 1 or s1[i] == '1':
            res = '1'+res
            carry = 0
        else:
            res = '0'+res
        i -= 1

    while j >= 0:
        if carry == 1 and s2[j] == '1':
            res = '0'+res
            carry = 1
        elif carry == 1 or s2[j] == '1':
            res = '1'+res
            carry = 0
        else:
            res = '0'+res
        j -= 1
    if carry == 1:
        res = '1'+res
    # print(res)
    return res

def solve(a):
    n = len(a)
    res = ""
    for i in range(n):
        res = add_binary(res, a[i])
    return res

if __name__ == "__main__":
    a = input().split(" ")
    print(solve(a))
