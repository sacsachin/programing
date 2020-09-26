/*
 * https://atcoder.jp/contests/abc152/tasks/abc152_e
 * Flatten.
 */

# include<iostream>
# include<vector>
# include<algorithm>

const long long MOD = 1e9+7;
const long long MAX_N = 1e6+5;

long long gcd(long long a, long long b)
{
    if(b == 0) return a;
    return gcd(b, a % b);
}

long long inverse(long long a, long long b, long long& x, long long& y)
{
    if( b == 0)
    {
        x = 1;
        y = 0;

        return a;
    }
    
    long long x1, y1;
    long long d = inverse(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);

    return d;
}


long long modpow(long long a, long long n, long long mod=MOD)
{
    long long res = 1;
    while (n > 0)
    {
        if (n & 1) res = res * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return res;
}

long long modinv(long long a, long long mod=MOD)
{
    return modpow(a, mod - 2, mod);
}

std::vector<std::pair<long long, long long>> prime_devisor(long long n)
{
    std::vector<std::pair<long long, long long>> res;
    for(long long p = 2; p * p <= n; p++)
    {
        if(n % p != 0) continue;
        
        long long num = 0;
        while(n % p == 0)
        {
            ++num;
            n /= p;
        }
        res.push_back(std::make_pair(p, num));
    }
    if(n != 1) res.push_back(std::make_pair(n, 1));

    return res;
}

long long solve(std::vector<long long>& a)
{
    std::vector<long long> mem(MAX_N, 0);

    for(int i = 0; i < a.size(); i++)
    {
        auto pd = prime_devisor(a[i]);
        for(auto p: pd) mem[p.first] = std::max(mem[p.first], p.second);
    }

    long long lcm = 1;
    for(int i = 2; i < MAX_N; i++) lcm = lcm*modpow(i, mem[i]) % MOD;

    long long ans = 0;
    for(int i = 0; i < a.size(); i++)
    {
        ans += lcm*modinv(a[i])%MOD;
    }

    return ans % MOD;
}

int main()
{
    int n;
    long long num, index = 0;
    std::cin>>n;

    std::vector<long long> a(n);
    while(n--)
    {
        std::cin>>num;
        a[index++] = num;
    }
    std::cout<<solve(a)<<std::endl;
    //std::cout<<MOD<<" "<<MAX_N;

    return 0;
}
