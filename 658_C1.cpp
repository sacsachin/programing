/*
 * https://codeforces.com/contest/1382/problem/C1
 * C1. Prefix Flip
 */

# include<iostream>
# include<string>
# include<vector>
# include<bitset>

# define cout(n, a) for(int i=0; i<n; i++){std::cout<<a[i];} std::cout<<std::endl;
# define cout_nn(n, a) for(int i=0; i<n; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}
# define cout_mn(m, n, a) for(int i=0; i<m; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}


int solve(std::string& a, std::string& b, int n, std::vector<int>& op) 
{
    int ans = 0;

    for(int i = 0; i < n; i++)
    {
        if(a == b) break;
        if(a[i] == b[i]) continue;

        ans++;
        op.push_back(i+1);
        ans++;
        op.push_back(1);
        ans++;
        op.push_back(i+1);
    }

    return ans;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    int t, n;
    std::string a, b;
    std::cin>>t;

    while(t--)
    {
        std::cin>>n;
        std::cin>>a>>b;
        std::vector<int> op;

        int k = solve(a, b, n, op);

        std::cout<<k;
        for(auto x: op) std::cout<<" "<<x;
        std::cout<<std::endl;
    }
    return 0;
}
