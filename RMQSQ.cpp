/*
 * https://www.spoj.com/problems/RMQSQ/
 * RMQSQ - Range Minimum Query
 */

# include<iostream>
# include<vector>
# include<limits>

//long long MAX_VALUE = std::numeric_limits<long long>::max();
//# define MAX_VALUE 1 << 63 -1
const int MAX_VALUE = (1LL << 31LL) - 1;
const int MAX_N = 1e5 + 5;
int a[MAX_N] = {0};
int tree[4 * MAX_N + 1] = {0};

void build_tree(int lo, int hi, int pos)
{
    if(lo == hi)
    {
        tree[pos] = a[lo];
        return;
    }
    
    int mid = (lo + hi) / 2;
    build_tree(lo, mid, 2*pos+1);
    build_tree(mid+1, hi, 2*pos+2 );

    tree[pos] = std::min(tree[2*pos+1], tree[2*pos+2]);

    return; 

}

int range_query(int lo, int hi, int qlo, int qhi, int pos)
{
    if(qlo <= lo and qhi >= hi) return tree[pos];
    if(qlo > hi or qhi < lo) return MAX_VALUE;

    int mid = (lo + hi)/2;
    return std::min(range_query(lo, mid, qlo, qhi, 2*pos+1), 
                    range_query(mid+1, hi, qlo, qhi, 2*pos+2));
}

void update(int lo, int hi, long long val, int index, int pos)
{
    if(lo > hi) return;
    if(lo == hi) 
    {
        tree[pos] = val;
        return;
    }

    int mid = (lo + hi) / 2;

    if (index <= mid) update(lo, mid, val, index, 2*pos+1);
    else update(mid+1, hi, val, index, 2*pos+2);

    tree[pos] = std::min(tree[2*pos+1], tree[2*pos+2]);

    return;
}

int main()
{
    int n, q;
    std::cin>>n;

    //std::vector<int> a(n);
    //std::vector<int> tree(4 * n + 1, 0);

    for(int i = 0; i < n; i++) std::cin>>a[i];

    build_tree(0, n-1, 0);

    int l, r;
    std::cin>>q;
    while(q--)
    {
        std::cin>>l>>r;
        std::cout<<range_query(0, n-1, l, r, 0)<<std::endl;
        
    }
}
