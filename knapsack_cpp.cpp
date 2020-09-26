/*
 * Knapsack
 * You are given n <= 1000 , each with some weight w[i].
 * Is there s subset with sum equals W. W<=10^6
 */


# include <iostream>
# include <vector>
# include <cstring>

# define MAX_W 100000
# define cout(n, a) for(int i=0; i<n; i++){std::cout<<a[i];} std::cout<<std::endl;
# define cout_nn(n, a) for(int i=0; i<n; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}
# define cout_mn(m, n, a) for(int i=0; i<m; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}

bool can[MAX_W];

int main()
{
    int n, w;
    std::cin>>n>>w;
    std::memset(can, false, sizeof can);
    cout(100, can);
    can[0] = true;

    for(int id = 0; id < n; id++)
    {
        int x;
        std::cin>>x;
        for(int i = w; i>=x; i--)
        {
            if(can[i-x]) can[i] = true;
        }
    }
    std::cout<<(can[w] ? "YES": "NO");
    //cout(100, can);

    return 0;
}


