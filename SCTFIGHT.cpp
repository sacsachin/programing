/*
 *https://www.codechef.com/QFUN2020/problems/SCTFIGHT
 *Scientist Fights.
 */

# include<iostream>
# include<vector>
# include<algorithm>

const int MAX_N = 10001;

int solve(std::vector<int>& a)
{
    int ans = 0, current_same = 1;
    sort(a.begin(), a.end());
    for(int i = 1; i < a.size(); i++)
    {
        if (a[i] == a[i-1])
            current_same++;
        else
        {
            //std::cout<<current_same<<std::endl;
            ans = std::max(ans, current_same);
            current_same = 1;
        }
    }
    ans = std::max(ans, current_same);

    return ans;
}


int main()
{
    std::ios_base::sync_with_stdio(false);

    int t, n, temp;
    std::cin>>t;
    while(t--)
    {
        std::vector<int> a;

        std::cin>>n;
        while(n--)
        {
            std::cin>>temp;
            a.push_back(temp);
        }
        std::cout<<solve(a)<<std::endl;
    }
    return 0;
}
