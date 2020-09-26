/*
 * https://www.codechef.com/QFUN2020/problems/MAGICMED
 * Magic and Corona Medicines.
 */


# include<iostream>
# include<vector>
# include<algorithm>

long long const MOD = 1e8+7;

long long binpow(long long a, long long b, long long m)
{
    a %= m;
    long long res = 1;
    while (b > 0) 
    {
        if (b & 1)
            res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}

long long solve(long long  a, long long b, long long c, long long m, long long p)
{
    long long ans;

    ans = binpow(a, b, m);
    ans = binpow(ans, c, m);

    return ans*p%MOD;
}

int main()
{
    long long t, a, b, c, m, p, ans;

    std::cin>>t;
    while(t--)
    {
        std::cin>>a>>b>>c>>m>>p;
        ans = solve(a, b, c, m, p);
        std::cout<<(ans ? "YES" : "NO")<<" "<<ans<<std::endl;
    }
    return 0;
}
