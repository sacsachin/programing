/*
 * Colorful Number
 * https://www.interviewbit.com/problems/colorful-number/
 */

# include<iostream>
# include<set>



std::string solve(int n)
{
    int num = n, power = 10, rem = 1;
    std::set<int> s;
    
    while(true)
    {
        num = n;
        while(num >= rem)
        {
            int t = num%power, prod = 1;
            while(t)
            {
                prod *= t%10;
                t /= 10;
            }
            if (s.find(prod) != s.end()) return "NO";
            s.insert(prod);
            num /= 10;        
        }
        if (power > n) break;
        power *= 10;
        rem *= 10;
    }
    return "YES";
}


int main()
{
    int n;

    std::cin>>n;
    std::cout<<solve(n)<<std::endl;
    return 0;
}
