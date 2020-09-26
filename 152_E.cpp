/*
 * https://atcoder.jp/contests/abc152/tasks/abc152_e
 * Flatten.
 */

# include<iostream>
# include<vector>

const long long MOD = 1e9+7;
const long long MAX_N = 1e6+5

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

long long solve(std::vector<long long>& a)
{
    long long lcm = 1, g, inv;

    for(int i = 0; i < a.size(); i++)
    {
        long long x, y;

        g = gcd(lcm, a[i]);
        //inverse(g, MOD, x, y);
        inv = modinv(g, MOD);
        //inv = (x%MOD+MOD)%MOD;
        inv = (inv % MOD + MOD) % MOD;
        lcm = (lcm * a[i] % MOD) * inv % MOD;
    }

    long long ans = 0;
    for(int i = 0; i < a.size(); i++)
    {
        long long x, y;
        //inverse(a[i], MOD, x, y);
        inv = modinv(a[i], MOD);
        //inv = (x%MOD+MOD)%MOD;
        inv = (inv % MOD + MOD) % MOD;
        ans += lcm*inv%MOD;
    }

    return ans % MOD;
}

int main()
{
    int n;
    std::cin>>n;

    std::vector<long long> a(n);
    for(int i = 0; i < n; i++) std::cin>>a[i];
    std::cout<<solve(a)<<std::endl;

    return 0;
}
