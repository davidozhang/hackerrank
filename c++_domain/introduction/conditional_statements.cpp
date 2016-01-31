#include <iostream>
using namespace std;

int main() {
    int input;
    std::cin>>input;
    if (input > 9) {
        std::cout<<"Greater than 9";  
    } else if (input == 1) {
        std::cout<<"one";
    } else if (input == 2) {
        std::cout<<"two";
    } else if (input == 3) {
        std::cout<<"three";
    } else if (input == 4) {
        std::cout<<"four";
    } else if (input == 5) {
        std::cout<<"five";
    } else if (input == 6) {
        std::cout<<"six";
    } else if (input == 7) {
        std::cout<<"seven";
    } else if (input == 8) {
        std::cout<<"eight";
    } else if (input == 9) {
        std::cout<<"nine";
    }
    return 0;
}
