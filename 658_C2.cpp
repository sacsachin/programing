/*
 * https://codeforces.com/contest/1382/problem/C2
 * Prefix Flip 2
 */

# include<iostream>
# include<vector>
# include<algorithm>

# define cout(n, a) for(int i=0; i<n; i++){std::cout<<a[i];} std::cout<<std::endl;
# define cout_nn(n, a) for(int i=0; i<n; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}
# define cout_mn(m, n, a) for(int i=0; i<m; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}

int solve(std::string& a, std::string&b, int n, std::vector<int>& op1, std::vector<int>& op2)
{
    a += '0';
    b += '0';
    for(int i = 1; i <= n; i++)
    {
        if(a[i] != a[i-1]) op1.push_back(i);
        if(b[i] != b[i-1]) op2.push_back(i);
    }

     op1.insert(op1.end(), op2.begin(), op2.end());
     
    return op1.size();
}

int main()
{
    int t;
    std::cin>>t;

    while(t--)
    {
        int n;
        std::cin>>n;

        std::string a, b;
        std::cin>>a>>b;
        std::vector<int> op1, op2;
        int ans = (a == b) ? 0 : solve(a, b, n, op1, op2);

        std::cout<<ans;
        for(int x: op1) std::cout<<" "<<x;
        std::cout<<std::endl;
    }
    return 0;
}
