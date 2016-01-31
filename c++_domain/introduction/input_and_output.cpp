#include <iostream>

int main() {
    int input;
    int sum = 0;
    while(std::cin>>input) {
        sum += input;
    }
    std::cout<<sum;
    return 0;
}
