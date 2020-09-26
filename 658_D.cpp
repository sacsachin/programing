/*
 * https://codeforces.com/contest/1382/problem/D
 * Unmerged.
 */

# include<iostream>
# include<vector>
# include<algorithm>
# include<bitset>

const int MAX_P = 2 * 2000 + 1;

std::bitset<MAX_P> mem;

std::string solve(std::vector<int>& a, int n)
{
    mem.reset();
    std::vector<int> subset;
    for(int i = 1; i < a.size(); i++) subset.push_back(a[i] - a[i-1]);
    
    mem[0] = true;
    for(int i = 0 ; i < subset.size(); i++)
    {
        if(mem[n]) return "YES";
        //for(int sum = MAX_P-1; sum >= subset[i]; sum--) if(mem[sum - subset[i]]) mem[sum] = true;
        mem |= mem << subset[i];
    }

    return "NO";
}

int main()
{
    std::ios_base::sync_with_stdio(false);

    int t;
    std::cin>>t;

    while(t--)
    {
        int n, mx = 0, num;
        std::cin>>n;
        std::vector<int> a;

        for(int i = 0; i < 2*n; i++)
        {
            std::cin>>num;
            if(num > mx)
            {
                mx = num;
                a.push_back(i);
            }
        }
        a.push_back(2 * n + 1);
        std::cout<<solve(a, n)<<std::endl;
    }
}
