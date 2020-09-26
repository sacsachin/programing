"""
Problem by khuillawda.
"""

def solve(a, b):
    a = [float('inf')]+a
    b = [float('inf')]+b
    n = len(a)
    even = 0
    odd = b[1]
    ans = 0
    for i in range(2, n):
        if a[i] == a[i-1] and i%2 == 0:
            even += b[i]
        elif a[i] == a[i-1] and i%2 == 1:
            odd += b[i]
        else:
            ans += max(odd, even)
            if i%2 == 0:
                even = b[i]
                odd = 0
            else:
                odd = b[i]
                even = 0
    ans += max(even, odd)
    return ans

if __name__ == "__main__":
    a = [(lambda x: int(x))(x) for x in input().split()]
    b = [(lambda x: int(x))(x) for x in input().split()]
    print(solve(a, b))



