
/*
struct node
{
    int data;
    node* left;
    node* right;
}*/

#include<map>

void LevelOrderHelper(map<int, vector<int> >& m, int depth, node* root) {
    if (root == NULL) {
        return;
    }
    m[depth].push_back(root->data);
    LevelOrderHelper(m, depth+1, root->left);
    LevelOrderHelper(m, depth+1, root->right);
}

void LevelOrder(node * root) {
    map<int, vector<int> > m;
    int depth = 0;
    LevelOrderHelper(m, depth, root);
    for (map<int, vector<int> >::iterator it = m.begin(); it != m.end(); it++) {
        for (vector<int>::iterator it2 = it->second.begin(); it2 != it->second.end(); it2++) {
            cout<<*it2<<" ";
        }
    }
}
