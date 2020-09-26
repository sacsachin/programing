# !/usr/bin/python3

def solve(s1, s2):
    ans = ""
    n = len(s1)
    m = len(s2)
    if not n or not m:
        return ""
    a = [0]*(max(n, m)*2)
    start = end = 0
    for i in range(n-1, -1, -1):
        count = start
        carry = 0
        for j in range(m-1, -1, -1):
            temp = a[count]
            a[count] = (temp+(ord(s1[i])-ord('0'))*(ord(s2[j])-ord('0'))+carry)%10
            carry = (temp+(ord(s1[i])-ord('0'))*(ord(s2[j])-ord('0'))+carry)//10
            count += 1
        if carry > 0:
            a[count] += carry
            count += 1
        start += 1
        end = count-1
    for i in range(end, -1, -1):
        # print(a[i], end="")
        ans += str(a[i])
    return ans

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(solve(s1, s2))
