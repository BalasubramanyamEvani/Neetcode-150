# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        lnode = self.lowestCommonAncestor(root.left, p, q)
        rnode = self.lowestCommonAncestor(root.right, p, q)
        
        if lnode and rnode:
            return root
        
        if lnode:
            return lnode
        
        if rnode:
            return rnode
        
        return None