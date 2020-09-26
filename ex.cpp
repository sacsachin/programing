# include<iostream>
# include<bitset>

int main()
{
    std::bitset<2> bit;
    std::cout<<bit<<std::endl;
    bit[0] = true;
    std::cout<<bit<<std::endl;
    bit <<= 1;
    std::cout<<bit<<std::endl;
    return 0;
}
