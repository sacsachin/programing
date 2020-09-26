# !/usr/bin/pyhton3

"""

"""

def solve(A):
    if A is 0:
        return []
    if A is 1:
        return [1]
    if A is 2:
        return [1, 1]
    traingle = [0]*(A*(A+1)//2)
    traingle[0] = traingle[1] = traingle[2] = 1
    for i in range(3, A+1):
        start = i*(i-1)//2
        end = i*(i+1)//2-1
        traingle[start] = 1
        traingle[end] = 1
        prv_start = (i-1)*(i-2)//2
        for j in range(start+1, end):
            traingle[j] = traingle[prv_start]+traingle[prv_start+1]
            prv_start+=1
    ans = []
    count = 0
    for i in range(A):
        temp = []
        for j in range(i+1):
            temp.append(traingle[count])
            count+=1
        ans.append(temp)
    return ans

if __name__ == "__main__":
    A = int(input())
    print(solve(A))

