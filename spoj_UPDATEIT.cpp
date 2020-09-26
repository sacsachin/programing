/*
 * https://www.spoj.com/problems/UPDATEIT/
 * UPDATEIT - Update the array !
 */

# include<iostream>
# include<vector>
# include<algorithm>
# include<cstring>

const int MAX_N = 1e5 + 5;
long long a[MAX_N] = {0};

void update(int l, int r, long long val)
{
    a[l] += val;
    a[r+1] -= val;
}

int main()
{
    int t, n; 
    std::cin>>t;

    while(t--)
    {
        int u;
        std::cin>>n>>u;
        
        std::memset(a, 0, sizeof a);
        while(u--)
        {
            long long l, r, val;

            std::cin>>l>>r>>val;
            update(l, r, val);
        }

        for(int i = 1; i < n; i++) a[i] += a[i-1];

        int q;
        std::cin>>q;
        while(q--)
        {
            int index;
            
            std::cin>>index;
            std::cout<<a[index]<<std::endl;
        }
    }
    return 0;
}
