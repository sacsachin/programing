/*
 * https://www.spoj.com/problems/DQUERY/
 * DQUERY
 */

# include<iostream>
# include<vector>
# include<algorithm>
# include<cmath>
# include<cstring>

long long const MAXN = 30000 + 1;
long long const MAXQ = 200000 + 5;
long long const MAXF = 1e6+10;
long long freq[MAXF] = {0}, ans[MAXQ] = {0};
long long block;

struct Query
{
    long long index;
    long long left;
    long long right;
};

bool compare(Query& a, Query& b)
{
    if(a.left / block == b.left / block) return a.right < b.right;
    return a.left / block < b.left / block;
}

void solve(std::vector<long long>& a, int n, std::vector<Query>& query, int q)
{
    std::sort(query.begin(), query.end(), compare);

    long long start = query[0].left - 1, end = start, count = 1;
    freq[a[start]]++;

    for(Query each : query)
    {
        long long queryl = each.left - 1;
        long long queryr = each.right - 1;

        while(start < queryl)
        {
            freq[a[start]]--;
            if(freq[a[start]] == 0) count--;
            start++;
        }

        while(start > queryl)
        {
            start--;
            freq[a[start]]++;
            if(freq[a[start]] == 1) count++;
        }
        
        while(end > queryr)
        {
            freq[a[end]]--;
            if(freq[a[end]] == 0) count--;
            end--;
        }

        while(end < queryr)
        {
            end++;
            freq[a[end]]++;
            if(freq[a[end]] == 1) count++;
        }

        ans[each.index] = count;
    }

    return;
}



int main()
{
    int n;
    std::cin>>n;

    std::vector<long long> a(n, 0);
    for(int i = 0; i < n; i++) std::cin>>a[i];

    int q;
    std::cin>>q;
    
    std::vector<Query> query(q);
    for(int i = 0; i < q; i++)
    {
        query[i].index = i;
        std::cin>>query[i].left>>query[i].right;
    }

    block = std::sqrt(n);
    solve(a, n, query, q);

    for(int i = 0; i < q; i++) std::cout<<ans[i]<<std::endl;

    return 0;
}
