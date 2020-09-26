/*
 * https://www.codechef.com/COOK120A/problems/PATHETIC
 * Patrh-etic Products.
 */

# include<iostream>
# include<vector>
# include<algorithm>
# include<bitset>
# include<cstring>
# include<deque>

# define cout(n, a) for(int i=0; i<n; i++){std::cout<<a[i];} std::cout<<std::endl;
# define cout_nn(n, a) for(int i=0; i<n; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}
# define cout_mn(m, n, a) for(int i=0; i<m; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}

const int MAX_N = 100+1;
std::bitset<MAX_N> tree[MAX_N], prime;
long long a[MAX_N] = {0};
long long p1 = 1, p2 = 1;

void generate_prime()
{
    prime.set();
    for(int i = 2; i*i < MAX_N; i++)
    {
        if(!prime[i]) continue;
        for(int j = i; i*j < MAX_N; j++) prime[i*j] = false;
    }

    for(long long i = MAX_N-1; i >= 2; i--)
    {
        if(prime[i])
        {
            if(p1 > p2) p2 *= i;
            else p1 *= i;
        }
    }

    return;
}

void bfs(int v, int n)
{
    std::deque<int> dq;
    dq.push_back(v);
    a[v] = p1;

    while(!dq.empty())
    {
        int node = dq.front();
        dq.pop_front();
        for(int i = 1; i <= n; i++)
        {
            if(tree[node][i])
            {
                dq.push_back(i);
                if(a[node] == p1) a[i] = p2;
                else a[i] = p1;

                tree[node][i] = false;
                tree[i][node] = false;
            }
        }
    }

    return;
}

void solve(int n)
{
    std::memset(a, 0, sizeof a);
    
    bfs(1, n);

    for(int i = 1; i <= n ;i++) std::cout<<a[i]<<" ";
    std::cout<<std::endl;

    return;
}

int main()
{
    int t;
    std::cin>>t;

    generate_prime();
    while(t--)
    {
        int n, u, v;
        std::cin>>n;
        for(int i = 0; i < MAX_N; i++) tree[i].reset();

        for(int i = 0; i < n-1; i++) 
        {
            std::cin>>u>>v;
            tree[u][v] = true;
            tree[v][u] = true;
        }

        solve(n);
    }
    return 0;
}
