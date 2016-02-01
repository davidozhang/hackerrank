#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


int main() {
    int n;
    int input;
    std::vector<int> v;
    std::cin>>n;
    while (std::cin>>input) {
        v.push_back(input);
    }
    std::sort(v.begin(), v.end());
    for (std::vector<int>::iterator it=v.begin(); it!=v.end();it++) {
        std::cout<<*it<<" ";
    }
    return 0;
}
