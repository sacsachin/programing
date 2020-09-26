# !/uar/bin/python3

"""
https://www.spoj.com/problems/ONP/
ONP - Transform the Expression
Stack
"""

def solve(s):
    n = s.__len__()
    st = []
    for i, c in enumerate(s):
        if c >= 'a' and c <= 'z':
            print(c, end="")
        elif c == '(':
            st.append(c)
        elif c == ')':
            print(st.pop(), end="")
            st.pop()
        else:
            st.append(c)
    while st:
        print(st.pop(), end="")
        st.pop
    print(end="\n")
    return

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        s = input()
        solve(s)
        t -= 1
