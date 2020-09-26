/*
 * https://www.codechef.com/problems/CHEFQUE
 * Checf ans Queries.
 */

# include <iostream>
# include <vector>
# include <bitset>

# define cout(n, a) for(ll i=0; i<n; i++){std::cout<<a[i];} std::cout<<std::endl;
# define cout_nn(n, a) for(ll i=0; i<n; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}
# define cout_mn(m, n, a) for(ll i=0; i<m; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}
# define ll long long

const ll MOD = 1LL << 32LL;
const ll MAX_S = 1LL << 32LL;
std::bitset<MAX_S/2LL+1LL> hash;

ll solve(ll q, ll s, ll a, ll b)
{
    ll ans = 0, p;
    while(q--)
    {
        if(s&1LL)
        {
            if(!hash[s>>1LL]) 
            {
                hash[s>>1LL] = true;
                ans += s>>1LL;
            }
        }
        else
        {
            if(hash[s>>1LL])
            { 
                hash[s>>1LL] = false;
                ans -= s>>1LL;
            }
        }
        s = (a*s+b)%MOD;
    }
    return ans;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    ll q, s, a, b;

    std::cin>>q>>s>>a>>b;
    std::cout<<solve(q, s, a, b)<<std::endl;

    return 0;
}
