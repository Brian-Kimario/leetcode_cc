# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # Base Case
        if not root or root == p or root == q:
            return root
        
        # Look left and right
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q are found in different subtrees, current root is the LCA
        if left and right:
            return root
        
        # Otherwise return the non-null child
        return left if left else right
