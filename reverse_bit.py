def reverse_bits(n):
    ans = 0
    t = 0
    for i in range(16):
        temp = n&(1<<31-i)
        if temp:
            t = 1<<i
        ans = t^ans
    return ans

if __name__ == "__main__":
    n = int(input())
    print(reverse_bits(n))
