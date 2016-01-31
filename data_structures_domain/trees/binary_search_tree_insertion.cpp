/*
Node is defined as 

typedef struct node
{
   int data;
   node * left;
   node * right;
}node;

*/


node * insert(node * root, int value)
{
   if (root == NULL) {
       node* n = new node();
       n->data = value;
       n->left = NULL;
       n->right = NULL;
       root = n;
   } else if (value < root->data) {
       root->left = insert(root->left, value);
   } else {
       root->right = insert(root->right, value);
   }
   return root;
}


