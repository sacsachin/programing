/*
 * https://www.codechef.com/QFUN2020/problems/CRCLJUMP
 * Circles and jump
 */

# include<iostream>
# include<vector>
# include<algorithm>
# include<bitset>

//const long long MAX_INT = 1<<32;

long long set_bits(long long num)
{
    long long ans = 0;

    while(num)
    {
        if(num&1) ans++;
        num >>= 1;
    }
    return ans;
}

long long solve(long long x, long long y, long long& diff)
{
    long long ans, set_x, set_y;

    x++; y++;
    set_x = set_bits(x);
    set_y = set_bits(y);

    diff = std::llabs(set_x-set_y);
    if(set_x < set_y) ans = 1;
    else if(set_y < set_x) ans = 2;
    else ans = 0;

    return ans;
}

int main()
{
    long long t, x, y, diff = 0;
    std::ios_base::sync_with_stdio(false);

    std::cin>>t;
    while(t--)
    {
        std::cin>>x>>y;
        std::cout<<solve(x, y, diff)<<" "<<diff<<std::endl;
    }
    return 0;
}
