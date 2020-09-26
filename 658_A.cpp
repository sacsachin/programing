/*
 *https://codeforces.com/contest/1382/problem/A
 *Common Subsequence.
 */

# include<iostream>
# include<vector>

void solve(std::vector<int>& a, std::vector<int>& b )
{
    for(int i = 0; i < a.size(); i++)
    {
        for(int j = 0; j < b.size(); j++)
        {
            if(a[i] == b[j])
            {
                std::cout<<"YES"<<" "<<std::endl;
                std::cout<<1<<" "<<a[i]<<std::endl;

                return;
            }
        }
    }
    std::cout<<"NO"<<std::endl;

    return;
}

int main()
{
    std::ios_base::sync_with_stdio(false);

    int t, n, m;
    std::cin>>t;

    while(t--)
    {
        std::cin>>n>>m;
        std::vector<int> a(n), b(m);
        int index = 0, val;

        while(n--)
        {
            std::cin>>val;
            a[index++] = val; 
        }

        index = 0;
        while(m--)
        {
            std::cin>>val;
            b[index++] = val;
        }

        solve(a, b);
    }

    return 0;
}
