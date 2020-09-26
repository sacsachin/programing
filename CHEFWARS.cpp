/*
 * https://www.codechef.com/AUG20B/problems/CHEFWARS
 * Chef Wars - Return of Jedi.
 */

# include<iostream>


int solve(int p, int h)
{
    while(p > 0 and h > 0)
    {
         h -= p;
         p >>= 1;
    }

    if(h <= 0) return 1;
    return 0;
}

int main()
{
    int t;
    std::cin>>t;

    int p, h;
    while(t--)
    {
        std::cin>>h>>p;
        std::cout<<(h >= 2*p) ? 0 : solve(p, h)<<std::endl;
    }
    return 0;
}
