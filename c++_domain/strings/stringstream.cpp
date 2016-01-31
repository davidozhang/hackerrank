#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    vector<int> result;
    stringstream ss(str);
    string item;
    while (getline(ss, item, ',')) {
        result.push_back(stoi(item));
    }
    return result;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
