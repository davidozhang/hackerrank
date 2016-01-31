#include <iostream>
#include <string>

int main() {
    int input;
    int size;
    std::cin>>size;
    int a[size];
    for (int i=0; i<size; i++) {
        std::cin>>input;
        a[i] = input;
    }
    for (int i=size-1; i>=0; i--) {
        std::cout<<a[i]<<" ";
    }
    return 0;
}
