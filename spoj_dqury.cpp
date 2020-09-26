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

bool compare(std::pair<long long, std::pair<long long, long long>>& a, std::pair<long long, std::pair<long long, long long>>& b)
{
    if(a.second.first / block != b.second.first / block) return a.first / block < b.first / block;
    return a.second.second < b.second.second;
}

void solve(std::vector<long long>& a, int n, std::vector<std::pair<long long, std::pair<long long, long long>>>& query, int q)
{
    std::sort(query.begin(), query.end(), compare);

    long long start = query[0].second.first - 1, end = start, count = 1;
    freq[a[start]]++;

    for(auto& each : query)
    {
        long long index = each.first;
        long long queryl = each.second.first - 1;
        long long queryr = each.second.second - 1;

        while(start < queryl)
        {
            freq[a[start]]--;
            if(freq[a[start]] == 0) count--;
            start++;
        }

        while(start > queryl)
        {
            start--;
            if(freq[a[start]] == 0) count++;
            freq[a[start]]++;
        }

        while(end < queryr)
        {
            end++;
            if(freq[a[end]] == 0) count++;
            freq[a[end]]++;
        }

        while(end > queryr)
        {
            freq[a[end]]--;
            if(freq[a[end]] == 0) count--;
            end--;
        }

        ans[index] = count;
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
    
    std::vector<std::pair<long long, std::pair<long long, long long>>> query(q);
    for(int i = 0; i < q; i++)
    {
        query[i].first = i;
        std::cin>>query[i].second.first>>query[i].second.second;
    }

    block = std::sqrt(n);
    solve(a, n, query, q);

    for(int i = 0; i < q; i++) std::cout<<ans[i]<<std::endl;

    return 0;
}
