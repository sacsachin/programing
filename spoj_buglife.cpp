/*
 * https://www.spoj.com/problems/BUGLIFE/
 * A bug's life.
 */

# include<iostream>
# include<vector>
# include<cstring>
# include<algorithm>
# include<bitset>
# include<queue>

const int MAXN = 2005;
std::bitset<MAXN> edge[MAXN];
int color[MAXN];

struct Bug
{
    int first;
    int second;
};

bool bfs(int node, int n)
{
    std::queue<int> q;
    q.push(node);
    color[node] = 0;

    while(!q.empty())
    {
        int u = q.front();
        q.pop();
        
        for(int v = 1; v <= n; v++)
        {
            if(edge[u][v] and color[v] == -1)
            {
                color[v] = 1 - color[u];
                q.push(v);
            }

            if(edge[u][v] and color[u] == color[v]) return false;
        }
    }

    return true;
}

bool solve(std::vector<Bug>& relation, int n, int k)
{
    for(int i = 0; i < MAXN; i++) edge[i].reset();
    for(int i = 0; i < MAXN; i++) color[i] = -1;

    for(int i = 0; i < k; i++)
    {
        edge[relation[i].first][relation[i].second] = true;
        edge[relation[i].second][relation[i].first] = true;
    }

    for(int u = 1; u <= n; u++) 
    {
        if(color[u] == -1)
        {
            if(!bfs(u, n)) return false;
        }
    }

    return true;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t;
    std::cin>>t;

    for(int i = 1; i <= t; i++)
    {
        int n, k;
        std::cin>>n>>k;

        std::vector<Bug> relation(k);
        for(int i = 0; i < k; i++) std::cin>>relation[i].first>>relation[i].second;

        std::cout<<"Scenario #"<<i<<":"<<std::endl;
        std::cout<<(solve(relation, n, k) ? "No suspicious bugs found!" : "Suspicious bugs found!")<<std::endl;
    }
    return 0;
}
