/*
 * https://leetcode.com/problems/sliding-window-maximum/
 * Sliding window maximum.
 */

# include <iostream>
# include <vector>
# include <deque>

# define cout(n, a) for(int i=0; i<n; i++){std::cout<<a[i]<<" ";} std::cout<<std::endl;
# define cout_nn(n, a) for(int i=0; i<n; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];<<" "}std::cout<<std::endl;}
# define cout_mn(m, n, a) for(int i=0; i<m; i++){for(int j=0; j<n; j++){std::cout<<a[i][j]<<" ";}std::cout<<std::endl;}

void solve(std::vector<int>& a, int k)
{
    std::deque<int> dq;
    std::vector<int> ans;

    for(int i = 0; i < a.size(); ++i)
    {
        while(!dq.empty() && dq.back() < a[i]) dq.pop_back();
        if (!dq.empty() && i-dq.front() >= k) dq.pop_front();
        dq.push_back(i);
        if(i >= k-1) ans.push_back(a[dq.front()]);
    }

    cout(ans.size(), ans);
    return;
}

int main()
{
    int n, k;
    std::vector<int> a;

    std::cin>>n>>k;
    while(n--)
    {
        int num;

        std::cin>>num;
        a.push_back(num);
    }
    solve(a, k);
    return 0;
}
