/*
 * https://www.codechef.com/COOK120B/problems/EVENTUAL
 * Even-tual Reduction.
 */

# include<iostream>

void solve(std::string& s, int n)
{
    int ans = 0;

    for(int i = 0; i < n; i++)
    {
        ans ^= (int)s[i]-96;
    }
    std::cout<<ans<<std::endl;
    std::cout<<(ans ? "NO": "YES")<<std::endl;

    return;
}


int main()
{
    int t;
    std::cin>>t;

    while(t--)
    {
        int n;
        std::cin>>n;

        std::string s;
        std::cin>>s;
        solve(s, n);
    }
    return 0;
}
