/*
 * Largest rectangle area in histogram.
 * https://leetcode.com/problems/largest-rectangle-in-histogram/
 */

# include <iostream>
# include <vector>
# include <stack>
# include <algorithm>

# define cout(n, a) for(int i=0; i<n; i++){std::cout<<a[i];} std::cout<<std::endl;
# define cout_nn(n, a) for(int i=0; i<n; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}
# define cout_mn(m, n, a) for(int i=0; i<m; i++){for(int j=0; j<n; j++){std::cout<<a[i][j];}std::cout<<std::endl;}

int solve(std::vector<int>& a)
{
    int n = a.size(), ans = 0, current = 0;
    std::stack<int> stack;

    while(current <= n)
    {
        while(!stack.empty() && (current == n || a[current] < a[stack.top()]))
        {
            int top = stack.top();
            stack.pop();
            if(stack.empty())
                ans = std::max(ans, a[top]*current);
            else
                ans = std::max(ans, a[top]*(current-stack.top()-1));
        }
        stack.push(current++);
    }

    return ans;
}

int main()
{
    int n;
    std::cin>>n;
    std::vector<int> v;

    while(n--)
    {
        int t;
        std::cin>>t;
        v.push_back(t);
    }
    std::cout<<solve(v);

    return 0;
}
