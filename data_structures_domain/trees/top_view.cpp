/*
struct node
{
    int data;
    node* left;
    node* right;
};

*/

void left(node* root) {
    if (root == NULL) {
        return;
    }
    node* traverse = root;
    if (traverse->left != NULL) {
        left(traverse->left);
    }
    std::cout<<traverse->data<<" ";
}

void right(node* root) {
    if (root == NULL) {
        return;
    }
    node* traverse = root;
    std::cout<<traverse->data<<" ";
    if (traverse->right != NULL) {
        right(traverse->right);
    }
}

void top_view(node * root) {
    if (root != NULL) {
        left(root->left);
        std::cout<<root->data<<" ";
        right(root->right);
    }
}
