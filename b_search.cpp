#include<iostream>

int bsearch(string& s, int l, int r, int key){
    int index = -1;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (s[mid] <= key)
            r = mid - 1;
        else {
            l = mid + 1;
            if (index == -1 || s[index] >= s[mid])
                index = mid;
        }
    }
    return index;
}

int main()
{
    int arr = [6, 5, 3, 2, 1];
    int s = bsearch(arr, 0, 4, 4);
    std::cout<<s;
    return 0;
}
