# !usr/bin/python3

def solve(a, k):
    n = len(a)
    sm = sum(a)
    if sm % k != 0:
        return "NO"


if __name__ == "__main__":
    a = [(lambda x: int(x))(x) for x in input().split(" ")]
    k = int(input())
    print(solve(a, k))
