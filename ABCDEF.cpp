#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

long solve(std::vector<long> &v, int n)
{
    long ans = 0, count=0, count1=0;
    std::vector<long> ab;
    std::vector<long> ef;
    
    for (int i=0; i < n; i++)
    {
        for (int  j=0; j < n; j++)
        {
            for (int k=0; k < n; k++)
            {
                ab.push_back(v[i]*v[j]+v[k]);
                if (v[k] != 0)
                {
                    ef.push_back((v[i]+v[j])*v[k]);
                }
            }
        }
    } 
    sort(ab.begin(), ab.end());
    sort(ef.begin(), ef.end());
    long i = 0;
    std::vector<long>::iterator lo, hi;
    while (i < n*n*n)
    {
        lo = lower_bound(ab.begin(), ab.end(), ab[i]);
        hi = upper_bound(ab.begin(), ab.end(), ab[i]);
        // std::cout<<(hi-lo)<<std::endl;
        ans += (hi-lo)*(upper_bound(ef.begin(), ef.end(), ab[i])-lower_bound(ef.begin(), ef.end(), ab[i]));
        i = hi-ab.begin();
    }

    return ans;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    int  n;
    std::cin>>n;
    std::vector<long> v(n);
    int t = 0;
    while (t < n)
    {
        std::cin>>v[t];
    // std::cout<<t<<std::endl;
        t++;
    }
    std::cout<<solve(v, n)<<std::endl;
    return 0;
}
