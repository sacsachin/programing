# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/power-of-2/
"""

def solve(s):
    a = [(lambda x: int(x))(x) for x in list(s)]
    n = len(a)
    end = n-1
    while end > 0:
        if a[end]&1:
            return 0
        carry = 0
        index = -1
        for i in range(end+1):
            if a[i] == 0 and carry == 0:
                index+= 1
                a[index] = a[i]
            elif i > 0 and a[i] == 1 and carry == 0:
                index += 1
                carry = 1
                a[index] = 0
            elif a[i]+10*carry >= 2:
                num = a[i]
                index += 1
                a[index] = (carry*10+num)>>1
                carry = (carry*10+num)%2
            else:
                carry = a[i]
        end = index

    if a[0] in (1, 2, 4, 8):
        return 1
    else:
        return 0

if __name__ == "__main__":
    s = input()
    print(solve(s))
