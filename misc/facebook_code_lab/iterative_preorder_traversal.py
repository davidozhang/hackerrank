# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
stack = []

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        stack.append(A)
        return self.preorderTraversalHelper()
    
    def preorderTraversalHelper(self):
        result = []
        while len(stack) > 0:
            s = stack.pop()
            result.append(s.val)
            if s.right:
                stack.append(s.right)
            if s.left:
                stack.append(s.left)
        return result
