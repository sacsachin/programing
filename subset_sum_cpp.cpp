/*
 * Subset sum.
 */

# include <iostream>
# include <vector>

std::string solve(std::vector<int>& a, int s)
{
    int n = a.size();
    for(int mask = 0; mask < (1<<n); mask++)
    {
        int sum_of_this_subset = 0;
        for(int i = 0; i < n; i++)
            if(mask & (1<<i)) sum_of_this_subset += a[i];
        if(sum_of_this_subset == s) return "YES";
    }
    return "NO";
}



int main()
{
    int n, s;
    std::vector<int> v;
    std::cin>>n;
    std::cin>>s;

    while(n--)
    {
        int num;
        std::cin>>num;
        v.push_back(num);
    }
    std::cout<<solve(v, s);
    return 0;
}
