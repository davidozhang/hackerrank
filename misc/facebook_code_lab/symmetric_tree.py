# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        return self.isSymmetricHelper(A, A)
    
    def isSymmetricHelper(self, A, B):
        if not A and not B:
            return True
        if not A or not B:
            return False
        return A.val == B.val and self.isSymmetricHelper(A.right, B.left) and self.isSymmetricHelper(A.left, B.right)
