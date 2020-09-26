/*
 * https://www.codechef.com/AABH2020/problems/ODTPIC
 * Odd Topic.
 */

# include<iostream>
# include<bitset>
# include<vector>

const int MAX = 4000+1;
const int MAX_N = 100000+1;
std::bitset<MAX> a[MAX_N], b[MAX_N], ans;

int solve(int l1, int r1, int l2, int r2)
{
    l1--; l2--; r1--; r2--;

    if(l1 > 0 and l2 > 0) ans = a[r1] xor a[l1-1] xor b[r2] xor b[l2-1];
    else if(l2 > 0) ans = a[r1] xor b[r2] xor b[l2-1];
    else if(l1 > 0) ans = a[r1] xor a[l1-1] xor b[r2];
    else ans = a[r1] xor b[r2];
    
    return ans.count();
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    int n, m, q, l1, r1, l2, r2, sub;
    std::cin>>n>>m>>q;
   
    std::cin>>sub;
    a[0][sub] = true;
    
    for(int i = 1; i < n; i++)
    {
        std::cin>>sub;
        a[i] = a[i-1];
        if(a[i][sub]) a[i][sub] = false;
        else a[i][sub] = true;
    }

    std::cin>>sub;
    b[0][sub] = true;
    
    for(int i = 1; i < m; i++)
    {
        std::cin>>sub;
        b[i] = b[i-1];
        if(b[i][sub]) b[i][sub] = false;
        else b[i][sub] = true;
    }

    while(q--)
    {
        std::cin>>l1>>r1;
        std::cin>>l2>>r2;
        std::cout<<solve(l1, r1, l2, r2)<<std::endl;
    }

    return 0;
}
