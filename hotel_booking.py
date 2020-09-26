# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/hotel-bookings-possible/
Hotel Bookings Possible
"""

def solve(arrive, depart, K):
    if K >= len(arrive):
        return True
    elif K == 0:
        return False

    arrive.sort()
    depart.sort()
    start = end = 0
    for i in range(1, len(arrive)):
        #print(arrive[i], "-----", depart[i])
        if arrive[i] >= depart[start]:
            start += 1
        end = i
        if end-start + 1> K:
            return False
    return True

def solve_way(arrive, depart, K):
    if K >= len(arrive):
        return True
    elif K == 0:
        return False
    bookings = [(each, 1) for each in arrive] + [(each, 0) for each in depart]
    #bookings += [(each, 0) for each in depart]
    bookings.sort(key=lambda x: (x[0], x[1]))
    print(bookings)
    allocated = 0
    for  each in bookings:
        if each[1] == 1:
            allocated +=1
        else:
            allocated -=1
        if allocated > K:
            return False
    return True


if __name__ == "__main__":
    A = [(lambda x: int(x))(x) for x in input().split(", ")]
    B = [(lambda x: int(x))(x) for x in input().split(", ")]
    print(solve_way(A, B, int(input())))
