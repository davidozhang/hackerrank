#include <iostream>
#include <set>
#include <algorithm>
using namespace std;

int main() {
    int n;
    int op, num;
    set<int> s;
    cin>>n;
    for (int i=0; i<n; i++) {
        cin>>op;
        cin>>num;
        if (op == 1) {
            s.insert(num);
        } else if (op == 2) {
            s.erase(num);
        } else if (op == 3) {
            if (s.count(num)) {
                cout<<"Yes"<<endl;
            } else {
                cout<<"No"<<endl;
            }
        }
    }
    return 0;
}
