# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/pretty-json/
Preety Json.
"""

def solve(s):
    n = len(s)
    tab = 0
    lines = []
    line = ""
    i = 0
    while i < n:
        if s[i] in ('{', '['):
            line = "\t"*tab+s[i]
            lines.append(line)
            tab += 1
            line = "\t"*tab
            i += 1
        elif s[i] in ('}', ']'):
            if line.strip() != "":
                lines.append(line)
            tab -= 1
            line = ""
            if i+1 < n and s[i+1] == ',':
                line = "\t"*tab+s[i]+s[i+1]
                i += 2
            else:
                line = "\t"*tab+s[i]
                i += 1
            lines.append(line)
            line = "\t"*tab
        elif s[i] == ',' and s[i+1] == ' ':
            line += ","
            lines.append(line)
            line = "\t"*tab
            i += 2
        elif s[i] == ':' and s[i+1] in ('{', '['):
            line += s[i]
            lines.append(line)
            line = "\t"*tab
            i += 1
        elif s[i] == ',' and s[i+1] != ' ':
            line += ","
            lines.append(line)
            line = "\t"*tab
            i += 1
        else:
            line += s[i]
            i += 1
    return lines

if __name__ == "__main__":
    s = input()
    ans = solve(s)
    for line in  ans: print(line)
