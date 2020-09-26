# !/usr/bin/python3

def merge(a, lo, mid, hi):
    i = lo
    j = mid+1
    res = []
    while i <= mid and j<= hi:
        if a[i] <= a[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(a[j])
            j += 1
    while i <= mid:
        res.append(a[i])
        i += 1
    while j <= hi:
        res.append(a[j])
        j += 1
    for i in range(len(res)):
        a[lo+i] = res[i]
    del res

def merge_sort(a, lo=0, hi=None):
    if lo < hi:
        mid = (lo+hi)//2
        merge_sort(a, lo, mid)
        merge_sort(a, mid+1, hi)
        merge(a, lo, mid, hi)

if __name__ == "__main__":
    a = [(lambda x: int(x))(x) for x in  input().split()]
    merge_sort(a, 0, len(a)-1)
    print(a)
