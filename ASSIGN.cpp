/*
 * https://www.spoj.com/problems/ASSIGN/
 * Assignment
 */

# include <iostream>
# include <vector>

# define cout(n, a) for(int i=0; i<n; i++){std::cout<<a[i];} std::cout<<std::endl;
# define cout_nn(n, a) for(int i=0; i<n; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}
# define cout_mn(m, n, a) for(int i=0; i<m; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}

long long solve(std::vector<std::vector<int>>& a, int n, std::vector<long long>& dp)
{
    //cout(1<<n, dp);
    dp[0] = 1;
    for (int j = 1; j < (1<<n); j++)
    {
        //dp[j] = 0;
        int student = 0, c = j;

        while (c > 0)
        {
            student += 1&c;
            c >>= 1;
        }

        for (int k=0; k < n; k++)
        {
            if (a[student-1][k] == 1 and j&(1<<k))
            {
                dp[j] += dp[j&~(1<<k)];
            }
        }
    }
    //cout_nn(n, a);
    //cout_mn(n, n, a);
    //cout(1<<n, dp);
    return dp[(1<<n)-1];
}

int main()
{
    int t, n, f;
    std::cin>>t;
    while(t--)
    {
        std::cin>>n;
        std::vector<std::vector<int>> a(n, std::vector<int> (n));
        std::vector<long long> dp(1<<n, 0);
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
                int f;
                std::cin>>f;
                a[i][j] = f;
            }
        }
        std::cout<<solve(a, n, dp)<<std::endl;
    }
    return 0;
}
