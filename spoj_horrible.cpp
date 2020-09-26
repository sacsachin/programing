/*
 * https://www.spoj.com/problems/HORRIBLE/
 * HORRIBLE - Horrible Queries
 */

# include<iostream>
# include<vector>
# include<algorithm>
# include<cstring>

const long long MAX_N = 1e5 + 5;
std::pair<long long, long long> tree[4 * MAX_N + 5];

long long query_lazy(long long lo, long long hi, long long qlo, long long qhi, long long pos)
{
    if(tree[pos].second != 0)
    {
        tree[pos].first += tree[pos].second * (hi - lo + 1);

        if(lo != hi)
        {
            tree[2*pos+1].second += tree[pos].second;
            tree[2*pos+2].second += tree[pos].second;
        }    
        tree[pos].second = 0;
    }

    if(lo > hi) return 0;
    if(qlo > hi or qhi < lo) return 0;
    if(qlo <= lo and qhi >= hi) return tree[pos].first;

    long long mid = (lo + hi) / 2;

    return query_lazy(lo, mid, qlo, qhi, 2*pos+1) + query_lazy(mid+1, hi, qlo, qhi, 2*pos+2);
}

void update_lazy(long long lo, long long hi, long long qlo, long long qhi, long long val, long long pos)
{
    if(tree[pos].second != 0)
    {
        tree[pos].first += tree[pos].second * (hi - lo +1);

        if(lo != hi)
        {
            tree[2*pos+1].second += tree[pos].second;
            tree[2*pos+2].second += tree[pos].second;
        }

        tree[pos].second = 0;
    }

    if(lo > hi) return;
    if(qlo > hi or qhi < lo) return;
    
    if(qlo <= lo and qhi >= hi)
    {
        tree[pos].first += val * (hi - lo + 1);

        if(lo != hi)
        {
            tree[2*pos+1].second += val;
            tree[2*pos+2].second += val;
        }
        return;
    }
    
    long long mid = (lo + hi) / 2;
    update_lazy(lo, mid, qlo, qhi, val, 2*pos+1);
    update_lazy(mid+1, hi, qlo, qhi, val ,2*pos+2);

    tree[pos].first = tree[2*pos+1].first + tree[2*pos+2].first;

    return;
}

int main()
{
    std::ios_base::sync_with_stdio(false);

    long long t;
    std::cin>>t;

    while(t--)
    {
        for(long long i = 0; i < 4 * MAX_N + 5; i++)
        {
            tree[i].first = 0;
            tree[i].second = 0;
        }

        long long n, c;
        std::cin>>n>>c;

        while(c--)
        {
            long long op, p, q;
            long long val;

            std::cin>>op;
            if(op == 1)
            {
                std::cin>>p>>q;
                std::cout<<query_lazy(0, n-1, p-1, q-1, 0)<<std::endl;
            }
            else
            {
                std::cin>>p>>q>>val;    
                update_lazy(0, n-1, p-1, q-1, val, 0);
            }
        }
    }
    return 0;
}
