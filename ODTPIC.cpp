/*
 * https://www.codechef.com/AABH2020/problems/ODTPIC
 * Odd Topic.
 */

# include<iostream>
# include<bitset>
# include<vector>

const int MAX = 4000+1;

int solve(int n, int m , std::vector<int>& a, std::vector<int>& b, int l1, int r1, int l2, int r2)
{
    int ans = 0;
    std::vector<int> res(MAX, 0);

    for(int i = l1-1; i < r1; i++) res[a[i]]++;
    for(int i = l2-1; i < r2; i++) res[b[i]]++;

    for(int i = 0; i < MAX; i++)
    {
        if(res[i]%2) ans++;
    }

    return ans;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    int n, m, q, temp, l1, r1, l2, r2;
    std::cin>>n>>m>>q;
    std::vector<int> a, b;
    
    temp = n;
    while(temp--)
    {
        int num;
        std::cin>>num;
        a.push_back(num);
    }

    temp = m;
    while(temp--)
    {
        int num;
        std::cin>>num;
        b.push_back(num);
    }

    while(q--)
    {
        std::cin>>l1>>r1;
        std::cin>>l2>>r2;
        std::cout<<solve(n, m, a, b, l1, r1, l2, r2)<<std::endl;
    }

    return 0;
}
