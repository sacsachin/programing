#include <cstdio>
#include <map>
#include <vector>
#define gc getchar
using namespace std;

typedef long long ll;

const ll mod=1LL<<32LL;

vector<bool> v(mod/2LL+1LL, false);

ll rl()
{
    char c = gc();
    while((c<'0' || c>'9') && c!='-')
        c = gc();
    ll ret = 0, neg = 1;
    if(c == '-')
    {
        neg = -1;
        c = gc();
    }
    while(c>='0' && c<='9')
    {
        ret = 10 * ret + c - 48;
        c = gc();
    }
    return ret * neg;      
}

int main() {
	// your code goes here
	ll Q, S, A, B, i;
	Q=rl();
	S=rl();
	A=rl();
	B=rl();
	ll p;
	ll ans=0;
	//printf("%lld\n", mod);
	while(Q--)
	{
		p=S/2LL;
		if(S%2LL)
		{
			if(v[p]==false)
			{
				v[p]=true;
				ans+=p;
			}
		}
		else
		{
			if(v[p]==true)
			{
				v[p]=false;
				ans-=p;
			}
		}
		S=(A*S+B)%mod;
	}
	printf("%lld", ans);
	return 0;
}
