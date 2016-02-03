/* 
The structure of the node is

typedef struct node
{
    int freq;
    char data;
    node * left;
    node * right;
    
}node;

*/


void decode_huff(node * root,string s) {
    node* traverse = root;
    for (int i=0; i<s.length(); i++) {
        if (s[i] == '0') {
            traverse = traverse->left;
        } else {
            traverse = traverse->right;
        }
        if (!traverse->left && !traverse->right) {
            cout<<traverse->data;
            traverse = root;
        }
    }
}
