/*
 * https://codeforces.com/contest/1382/problem/B
 * Sequential Nim.
 */

# include<iostream>
# include<vector>

void solve(std::vector<int>& a)
{
    bool first = true;

    for(int i = 0; i < a.size()-1; i++)
    {
        if(a[i] == 1) first = not first;
        else break;
    }

    if(first) std::cout<<"First"<<std::endl;
    else std::cout<<"Second"<<std::endl;

    return;
}

int main()
{
    int t, n;
    std::cin>>t;

    while(t--)
    {
        std::cin>>n;

        std::vector<int> a(n);
        int val, index = 0;

        while(n--)
        {
            std::cin>>val;
            a[index++] = val;
        }
        solve(a);
    }

    return 0;
}
