/*
 * https://leetcode.com/problems/trapping-rain-water/
 * Trapping rain water.
 */

# include<iostream>
# include<vector>
# include<stack>
# include<algorithm>

# define cout(n, a) for(int i=0; i<n; i++){std::cout<<a[i];} std::cout<<std::endl;
# define cout_nn(n, a) for(int i=0; i<n; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}
# define cout_mn(m, n, a) for(int i=0; i<m; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}

int solve(std::vector<int>& a)
{
    std::stack<int> st;
    int current = 0, ans = 0;

    while(current < a.size())
    {
        while(!st.empty() && a[current] > a[st.top()])
        {
            int top = st.top();
            st.pop();
            if(st.empty())
                break;
            int distance = current-st.top()-1;
            int bound_height = std::min(a[current], a[st.top()])-a[top];
            ans += distance*bound_height;
        }
        st.push(current++);
    }
    return ans;
}

int main()
{
    int n;
    std::vector<int> v;

    std::cin>>n;
    while(n--)
    {
        int a;
        std::cin>>a;
        v.push_back(a);
    }
    std::cout<<solve(v);
    return 0;
}
