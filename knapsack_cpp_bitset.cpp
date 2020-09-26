/*
 * Knapsack
 * You are given n <= 1000 , each with some weight w[i].
 * Is there s subset with sum equals W. W<=10^6
 */


# include <iostream>
# include <vector>
# include <cstring>
# include <bitset>

# define MAX_W 10
# define cout(n, a) for(int i=0; i<n; i++){std::cout<<a[i];} std::cout<<std::endl;
# define cout_nn(n, a) for(int i=0; i<n; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}
# define cout_mn(m, n, a) for(int i=0; i<m; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}


std::bitset<MAX_W> can;

int main()
{
    int n, w;
    std::cin>>n>>w;
    can[0] = true;
    //std::bitset<4> f(2);
    //std::cout<<f<<std::endl;
    //std::cout<<f[0]<<f[1]<<f[2]<<f[3]<<std::endl;
    //f <<= 1;
    //std::cout<<f<<std::endl;
    //std::cout<<f[0]<<f[1]<<f[2]<<f[3]<<std::endl;

    for(int id = 0; id < n; id++)
    {
        int x;
        std::cin>>x;
        can |= (can << x);
    }
    //std::cout<<(can[w] ? "YES": "NO");
    return 0;
}
