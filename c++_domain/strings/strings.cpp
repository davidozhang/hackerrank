#include <iostream>
#include <string>
#include <vector>

int main() {
    std::string input;
    std::string s[2];
    for (int i=0; i<2; i++) {
        std::cin>>input;
        s[i] = input;
    }
    std::cout<<s[0].size()<<" "<<s[1].size()<<std::endl;
    std::cout<<s[0] + s[1]<<std::endl;
    std::cout<<s[1][0] + s[0].substr(1)<<" "<<s[0][0] + s[1].substr(1)<<std::endl;
    return 0;
}
