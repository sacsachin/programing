# include<iostream>

std::string solve(std::string& s)
{
    ++s[0];
    return s;
}

int main()
{
  std::string s;
  std::cin>>s;
  
  std::cout<<solve(s)<<std::endl;
  return 0;
}
