/*
 * https://www.codechef.com/COOK120B/problems/ORTHODOX
 * Or-thodex Distinction.
 */

# include<iostream>
# include<vector>
# include<algorithm>
# include<set>
# include<unordered_set>


void solve(std::vector<long long>& a)
{
    if(a.size() > 63)
    {
        std::cout<<"NO"<<std::endl;
        return;
    }

    std::unordered_set<long long> s;

    for(int i = 0; i < a.size(); i++)
    {
        long long res = 0;

        for(int j = i; j < a.size(); j++)
        {
            res |= a[j];
            if(s.find(res) != s.end())
            {
                std::cout<<"NO"<<std::endl;
                //return;
            }
            s.insert(res);
        }
    }
    for(auto x: s) std::cout<<x<<" ";
    std::cout<<std::endl;

    std::cout<<"YES"<<std::endl;
    
    return;
}

int main()
{
    std::ios_base::sync_with_stdio(false);

    int t, n;
    long long num;

    std::cin>>t;
    while (t--)
    {
        std::cin>>n;
        std::vector<long long> a(n);

        int index = 0;

        while(n--)
        {
            std::cin>>num;
            a[index] = num;
            index++;
        }
        solve(a);
    }
    return 0;
}
