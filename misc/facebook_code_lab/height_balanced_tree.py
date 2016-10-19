# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        if not A:
            return True
        return self.isBalanced(A.left) and self.isBalanced(A.right) and abs(self.height(A.left)-self.height(A.right)) <= 1
    
    def height(self, A):
        if not A:
            return 0
        return 1 + max(self.height(A.left), self.height(A.right))
