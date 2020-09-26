

#include <iostream>
#include <vector>

int convertIntoInt(std::string s){
   int tmp=1;
   int ret = 0;
   for(int i= s.size()-1 ; i>=0 ; --i){
      ret += tmp * (s[i]-'a');
   }
}
int solve(std::vector<int> & dp, const string s){
    for(int i=1 ; i<s.size() ; ++i){
      string value = s[i] + s[i-1];

    }
}

int main(){
    int t;
    std::cin>>t;
    while(t--){
        std::string n;
        std::cin>>n;
        std::vector<int> dp(n,0);
        solve(dp,n);
        
    }
}
